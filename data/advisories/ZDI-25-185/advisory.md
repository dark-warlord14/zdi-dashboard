# ZDI-25-185: (0Day) BEC Technologies Multiple Routers Insufficiently Protected Credentials Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-185
- **ZDI-CAN:** ZDI-CAN-25895
- **Date:** 2025-03-25
- **CVE:** CVE-2025-2772
- **CVSS:** 5.3
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** BEC Technologies
- **Affected Products:** Multiple Routers
- **Credit:** Steven C Yu of Trend Micro Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-185/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to disclose sensitive information on affected installations of BEC Technologies routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within /cgi-bin/tools_usermanage.asp. The issue results from transmitting a list of users and their credentials to be handled on the client side. An attacker can leverage this vulnerability to disclose transported credentials, leading to further compromise.

## Additional Details

12/06/24 – ZDI contacted the vendor’s support team via email 02/13/25 – ZDI requested an update 03/12/25 – ZDI informed the vendor that since we have not received a response, we will publish the report as a 0-day advisory 03/25/25 - ZDI published the report as a 0-day advisory 11/20/25 - The vendor notified ZDI that the vulnerability has been patched Mitigation: For all firmware versions 1.04.1.x, update to 1.04.1.676 or later. For all firmware versions 1.00.1.x, update to 1.00.1.196 or later.

## Disclosure Timeline

- 2025-03-11 - Vulnerability reported to vendor
- 2025-03-25 - Coordinated public release of advisory
- 2025-11-24 - Advisory Updated
