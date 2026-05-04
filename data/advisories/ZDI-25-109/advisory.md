# ZDI-25-109: Apache Pinot Improper Neutralization of Special Elements Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-109
- **ZDI-CAN:** ZDI-CAN-24001
- **Date:** 2025-03-03
- **CVE:** CVE-2024-56325
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apache
- **Affected Products:** Pinot
- **Credit:** Sunflower@Knownsec 404 Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-109/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Apache Pinot. Authentication is not required to exploit this vulnerability. The specific flaw exists within the AuthenticationFilter class. The issue results from insufficient neutralization of special characters in a URI. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Fixed in version 1.3.0

## Disclosure Timeline

- 2024-07-16 - Vulnerability reported to vendor
- 2025-03-03 - Coordinated public release of advisory
- 2025-03-03 - Advisory Updated
