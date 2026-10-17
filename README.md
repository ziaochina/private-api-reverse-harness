# Private API Reverse Engineering & Protocol Harness

High-performance reverse engineering harness for private web/mobile APIs, HMAC request signing, and headless data streaming.

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

---

## ⚡ 100x Faster & 90% Cheaper than Browser Automation

Heavy headless browsers (Puppeteer/Playwright) consume 1-2GB RAM per worker and fail on concurrency.
By reverse-engineering private mobile/web APIs directly:
* **Throughput**: 500+ requests/sec on a $10 VPS;
* **Memory**: < 50MB RAM footprint;
* **Resilience**: Zero DOM layout shifts or broken CSS selector issues.

---

## 🔐 Features
- Automated HMAC-SHA256 request signature derivation;
- Dynamic timestamp nonce & token rotation;
- Local mock server included for deterministic unit testing.
