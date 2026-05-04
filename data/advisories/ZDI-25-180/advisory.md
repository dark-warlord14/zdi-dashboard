# ZDI-25-180: (0Day) 70mai A510 Use of Default Password Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-180
- **ZDI-CAN:** ZDI-CAN-24996
- **Date:** 2025-03-25
- **CVE:** CVE-2025-2766
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** 70mai
- **Affected Products:** A510
- **Credit:** (VicOne Inc) Aaron Luo, Spencer Hsieh
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-180/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass authentication on affected installations of 70mai A510. Authentication is not required to exploit this vulnerability. The specific flaw exists within the default configuration of user accounts. The configuration contains default password. An attacker can leverage this vulnerability to bypass authentication and execute arbitrary code in the context of the root.

## Additional Details

07/30/24 – ZDI reported the vulnerability to the vendor 11/17/24 - ZDI asked for updates 12/16/24 - ZDI asked for updates 03/12/25 - ZDI notified the vendor of the intention to publish the case as a 0-day advisory

## Disclosure Timeline

- 2024-07-30 - Vulnerability reported to vendor
- 2025-03-25 - Coordinated public release of advisory
- 2025-03-25 - Advisory Updated
