# ZDI-25-748: (Pwn2Own) QNAP QHora-322 system.db Use of Hard-coded Cryptographic Key Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-748
- **ZDI-CAN:** ZDI-CAN-25657
- **Date:** 2025-07-31
- **CVE:** N/A
- **CVSS:** 8.1
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** QNAP
- **Affected Products:** QHora-322
- **Credit:** Benjamin Walny, Neodyme AG
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-748/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of QNAP QHora-322 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the storage of credentials. The issue results from the use of a hard-coded cryptographic key. An attacker can leverage this in conjunction with other vulnerabilities to bypass authentication on the system.

## Additional Details

QNAP has issued an update to correct this vulnerability. More details can be found at: https://www.qnap.com/en-us/security-advisories

## Disclosure Timeline

- 2024-12-02 - Vulnerability reported to vendor
- 2025-07-31 - Coordinated public release of advisory
- 2025-07-31 - Advisory Updated
