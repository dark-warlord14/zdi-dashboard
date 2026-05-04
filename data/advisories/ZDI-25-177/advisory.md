# ZDI-25-177: (0Day) CarlinKit CPC200-CCPA Wireless Hotspot Hard-Coded Credentials Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-177
- **ZDI-CAN:** ZDI-CAN-24349
- **Date:** 2025-03-25
- **CVE:** CVE-2025-2765
- **CVSS:** 7.6
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:L/A:L
- **Affected Vendors:** CarlinKit
- **Affected Products:** CPC200-CCPA
- **Credit:** Aaron Luo and Spencer Hsieh of VicOne
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-177/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass authentication on affected installations of CarlinKit CPC200-CCPA devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the configuration of the wireless hotspot. The issue results from the use of hard-coded credentials. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

06/05/24 – ZDI contacted the vendor’s support team via email 07/12/24 – ZDI sent a second PSIRT contact request to CarlinKit support team 11/13/24 – ZDI asked for updates 02/18/25 – ZDI informed the vendor that since we have not received a response, we will publish the report as a 0-day advisory

## Disclosure Timeline

- 2025-03-11 - Vulnerability reported to vendor
- 2025-03-25 - Coordinated public release of advisory
- 2025-03-25 - Advisory Updated
