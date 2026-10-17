"""
HMAC-SHA256 Protocol Signature & Canonical Request Derivation
"""
import hmac
import hashlib
import time
from typing import Dict, Any, Optional

class ProtocolSigner:
    def __init__(self, secret_key: str = "production_client_secret_v1"):
        self.secret_key = secret_key.encode("utf-8")

    def derive_canonical_query(self, params: Dict[str, Any]) -> str:
        """
        Sorts query parameters lexicographically for deterministic HMAC derivation.
        """
        sorted_items = sorted(params.items(), key=lambda x: x[0])
        return "&".join(f"{k}={v}" for k, v in sorted_items)

    def sign(self, method: str, endpoint: str, params: Optional[Dict[str, Any]] = None, timestamp: Optional[int] = None) -> Dict[str, str]:
        ts = timestamp if timestamp is not None else int(time.time())
        canonical_params = self.derive_canonical_query(params or {})
        
        # Build canonical payload: METHOD:ENDPOINT:QUERY:TIMESTAMP
        payload = f"{method.upper()}:{endpoint}:{canonical_params}:{ts}".encode("utf-8")
        signature = hmac.new(self.secret_key, payload, hashlib.sha256).hexdigest()

        return {
            "X-Timestamp": str(ts),
            "X-Signature": signature,
            "X-Protocol-Version": "2.4.0",
        }

    def verify(self, method: str, endpoint: str, signature: str, timestamp_str: str, params: Optional[Dict[str, Any]] = None, max_age_seconds: int = 300) -> bool:
        try:
            ts = int(timestamp_str)
        except ValueError:
            return False

        # Anti-replay freshness check
        if abs(int(time.time()) - ts) > max_age_seconds:
            return False

        expected = self.sign(method, endpoint, params, timestamp=ts)
        return hmac.compare_digest(expected["X-Signature"], signature)
