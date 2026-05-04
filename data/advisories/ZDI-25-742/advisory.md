# ZDI-25-742: (Pwn2Own) QNAP TS-464 Active Directory Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-742
- **ZDI-CAN:** ZDI-CAN-25587
- **Date:** 2025-07-31
- **CVE:** N/A
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** QNAP
- **Affected Products:** TS-464
- **Credit:** Corentin "@OnlyTheDuck" BAYET from REverse Tactics
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-742/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass authentication on affected installations of QNAP TS-464 devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Active Directory integration. The issue results from the improper implementation of an authentication algorithm. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

QNAP has issued an update to correct this vulnerability. More details can be found at: https://www.qnap.com/en-us/security-advisories

## Disclosure Timeline

- 2024-12-19 - Vulnerability reported to vendor
- 2025-07-31 - Coordinated public release of advisory
- 2025-07-31 - Advisory Updated
