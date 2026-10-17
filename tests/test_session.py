"""
Unit Tests for Harness Session
"""
from reverse_harness.session import HarnessSession

def test_session_prepare_headers():
    session = HarnessSession(secret_key="test_key", seed="test_seed")
    headers = session.prepare_request_headers("POST", "/api/v1/auth", {"user": "admin"})
    assert "X-Signature" in headers
    assert "X-Timestamp" in headers
    assert "X-Device-Id" in headers
