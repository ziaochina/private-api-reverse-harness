"""
Hardware Device Fingerprint & Telemetry Synthesis
"""
import uuid
import hashlib

class DeviceFingerprint:
    @staticmethod
    def generate_device_id(seed: str = "workstation-node-01") -> str:
        digest = hashlib.sha256(seed.encode("utf-8")).hexdigest()
        return str(uuid.UUID(digest[:32]))

    @classmethod
    def get_headers(cls, seed: str = "workstation-node-01") -> dict:
        dev_id = cls.generate_device_id(seed)
        return {
            "X-Device-Id": dev_id,
            "X-Platform": "Darwin 23.4.0",
            "X-App-Build": "14920",
            "User-Agent": "MobileCatalogClient/2.4.0 (Macintosh; Intel Mac OS X 10_15_7)"
        }
