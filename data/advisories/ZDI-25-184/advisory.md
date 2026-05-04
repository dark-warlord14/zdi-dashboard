# ZDI-25-184: (0Day) BEC Technologies Multiple Routers Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-184
- **ZDI-CAN:** ZDI-CAN-25894
- **Date:** 2025-03-25
- **CVE:** CVE-2025-2771
- **CVSS:** 5.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N
- **Affected Vendors:** BEC Technologies
- **Affected Products:** Multiple Routers
- **Credit:** Steven C Yu of Trend Micro Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-184/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of BEC Technologies routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the web-based user interface. The issue results from the lack of authentication prior to allowing access to functionality. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

12/06/24 – ZDI contacted the vendor’s support team via email 02/13/25 – ZDI requested an update 03/12/25 – ZDI informed the vendor that since we have not received a response, we will publish the report as a 0-day advisory 03/25/25 - ZDI published the report as a 0-day advisory 11/20/25 - The vendor notified ZDI that the vulnerability has been patched Mitigation: For all firmware versions 1.04.1.x, update to 1.04.1.676 or later. For all firmware versions 1.00.1.x, update to 1.00.1.196 or later.

## Disclosure Timeline

- 2025-03-11 - Vulnerability reported to vendor
- 2025-03-25 - Coordinated public release of advisory
- 2025-11-25 - Advisory Updated
