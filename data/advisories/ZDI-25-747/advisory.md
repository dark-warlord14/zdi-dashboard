# ZDI-25-747: (Pwn2Own) QNAP TS-464 reset_password.cgi Hard-coded Cryptographic Key Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-747
- **ZDI-CAN:** ZDI-CAN-25646
- **Date:** 2025-07-31
- **CVE:** N/A
- **CVSS:** 7.5
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** QNAP
- **Affected Products:** TS-464
- **Credit:** @quangnh89 and @ExLuck99
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-747/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass authentication on affected installations of QNAP TS-464. Authentication is not required to exploit this vulnerability. The specific flaw exists within the reset_password.cgi endpoint. The issue results from the use of a hard-coded cryptographic key. An attacker can leverage this in conjunction with other vulnerabilities to bypass authentication on the system.

## Additional Details

QNAP has issued an update to correct this vulnerability. More details can be found at: https://www.qnap.com/en-us/security-advisories

## Disclosure Timeline

- 2024-12-02 - Vulnerability reported to vendor
- 2025-07-31 - Coordinated public release of advisory
- 2025-07-31 - Advisory Updated
