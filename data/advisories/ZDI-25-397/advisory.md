# ZDI-25-397: Delta Electronics COMMGR Insufficient Randomization Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-397
- **ZDI-CAN:** ZDI-CAN-25049
- **Date:** 2025-06-17
- **CVE:** CVE-2025-3495
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Delta Electronics
- **Affected Products:** COMMGR
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-397/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Delta Electronics COMMGR. Authentication is not required to exploit this vulnerability. The specific flaw exists within the PLC simulator service, which listens on TCP port 8895 by default. By conducting a brute force attack at moderate expense, an attacker can find a valid session identifier. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Delta Electronics has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-25-105-07

## Disclosure Timeline

- 2024-11-19 - Vulnerability reported to vendor
- 2025-06-17 - Coordinated public release of advisory
- 2025-06-17 - Advisory Updated
