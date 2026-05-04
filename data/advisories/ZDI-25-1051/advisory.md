# ZDI-25-1051: Ivanti Endpoint Manager HIIDriver Improper Verification of Cryptographic Signature Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1051
- **ZDI-CAN:** ZDI-CAN-26897
- **Date:** 2025-12-10
- **CVE:** CVE-2025-13662
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Ivanti
- **Affected Products:** Endpoint Manager
- **Credit:** 06fe5fd2bc53027c4a3b7e395af0b850e7b8a044
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1051/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Ivanti Endpoint Manager. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. Alternatively, no user interaction is required if the attacker has administrative credentials to the application. The specific flaw exists within the HIIDriver class. The issue results from the lack of proper verification of a cryptographic signature. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current user or in the context of the service account.

## Additional Details

Ivanti has issued an update to correct this vulnerability. More details can be found at: https://forums.ivanti.com/s/article/Security-Advisory-EPM-December-2025-for-EPM-2024

## Disclosure Timeline

- 2025-09-19 - Vulnerability reported to vendor
- 2025-12-10 - Coordinated public release of advisory
- 2025-12-10 - Advisory Updated
