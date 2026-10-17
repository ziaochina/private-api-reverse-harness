"""
Unit Tests for Device Fingerprint
"""
import uuid
from reverse_harness.fingerprint import DeviceFingerprint

def test_device_id_format():
    dev_id = DeviceFingerprint.generate_device_id("seed-123")
    parsed = uuid.UUID(dev_id)
    assert str(parsed) == dev_id

def test_device_headers():
    headers = DeviceFingerprint.get_headers("seed-456")
    assert "X-Device-Id" in headers
    assert "X-Platform" in headers
