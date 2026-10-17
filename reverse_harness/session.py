"""
Reverse Harness Session Wrapper with Auto-Signing
"""
from typing import Dict, Any, Optional
from .signer import ProtocolSigner
from .fingerprint import DeviceFingerprint

class HarnessSession:
    def __init__(self, secret_key: str = "production_client_secret_v1", seed: str = "client-01"):
        self.signer = ProtocolSigner(secret_key=secret_key)
        self.device_headers = DeviceFingerprint.get_headers(seed=seed)

    def prepare_request_headers(self, method: str, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, str]:
        headers = dict(self.device_headers)
        sig_headers = self.signer.sign(method=method, endpoint=endpoint, params=params)
        headers.update(sig_headers)
        return headers
