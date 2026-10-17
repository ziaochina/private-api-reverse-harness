"""
Unit Tests for HMAC Protocol Signer
"""
import time
from reverse_harness.signer import ProtocolSigner

def test_signature_determinism():
    signer = ProtocolSigner(secret_key="test_secret")
    params = {"b": "2", "a": "1"}
    sig1 = signer.sign("GET", "/test", params, timestamp=1700000000)
    sig2 = signer.sign("GET", "/test", {"a": "1", "b": "2"}, timestamp=1700000000)
    assert sig1["X-Signature"] == sig2["X-Signature"]

def test_signature_verification():
    signer = ProtocolSigner(secret_key="test_secret")
    now = int(time.time())
    sig = signer.sign("GET", "/endpoint", {"q": "search"}, timestamp=now)
    assert signer.verify("GET", "/endpoint", sig["X-Signature"], str(now), {"q": "search"}) is True
    assert signer.verify("GET", "/endpoint", "bad_signature", str(now), {"q": "search"}) is False
