"""
CLI Entrypoint for Private API Reverse Engineering Harness
"""
from reverse_harness.session import HarnessSession
from reverse_harness.signer import ProtocolSigner

def main():
    print("[*] Initializing Private API Protocol Signature Harness...")
    session = HarnessSession(secret_key="mobile_app_prod_key_99x", seed="device-san-jose-01")

    endpoint = "/api/v2/catalog/bulk_query"
    params = {"category": "electronics", "page": "1", "limit": "100"}

    print(f"[*] Deriving canonical signature for: {endpoint}")
    headers = session.prepare_request_headers(method="GET", endpoint=endpoint, params=params)

    print("[+] Generated RFC-Compliant Protocol Headers:")
    for k, v in headers.items():
        print(f"    {k}: {v}")

    # Offline verification test
    signer = ProtocolSigner(secret_key="mobile_app_prod_key_99x")
    is_valid = signer.verify(
        method="GET",
        endpoint=endpoint,
        signature=headers["X-Signature"],
        timestamp_str=headers["X-Timestamp"],
        params=params
    )
    print(f"[+] Cryptographic Signature Verification: {'PASSED (100% Valid)' if is_valid else 'FAILED'}")

if __name__ == "__main__":
    main()
