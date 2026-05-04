# ZDI-24-826: (Pwn2Own) QNAP TS-464 Improper Validation Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-826
- **ZDI-CAN:** ZDI-CAN-22496
- **Date:** 2024-06-21
- **CVE:** CVE-2024-32766
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** QNAP
- **Affected Products:** TS-464
- **Credit:** Tri and Bien Pham (@bienpnn) from Team Orca of Sea Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-826/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of QNAP TS-464 NAS devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the authentication logic. The issue results from improper validation of the password. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

QNAP has issued an update to correct this vulnerability. More details can be found at: https://www.qnap.com/en-us/security-advisory/qsa-24-09

## Disclosure Timeline

- 2023-11-09 - Vulnerability reported to vendor
- 2024-06-21 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
