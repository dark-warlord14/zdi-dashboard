# ZDI-25-085: Logsign Unified SecOps Platform Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-085
- **ZDI-CAN:** ZDI-CAN-25336
- **Date:** 2025-02-05
- **CVE:** CVE-2025-1044
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Logsign
- **Affected Products:** Unified SecOps Platform
- **Credit:** Abdessamad Lahlali and Smile Thanapattheerakul of Trend Micro
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-085/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Logsign Unified SecOps Platform. Authentication is not required to exploit this vulnerability. The specific flaw exists within the web service, which listens on TCP port 443 by default. The issue results from the lack of proper implementation of the authentication algorithm. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Logsign has issued an update to correct this vulnerability. More details can be found at: https://support.logsign.net/hc/en-us/articles/22076844908946-18-10-2024-Version-6-4-32-Release-Notes

## Disclosure Timeline

- 2024-09-26 - Vulnerability reported to vendor
- 2025-02-05 - Coordinated public release of advisory
- 2025-02-05 - Advisory Updated
