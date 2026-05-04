# ZDI-24-517: Progress Software WhatsUp Gold FaviconController Server-Side Request Forgery Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-517
- **ZDI-CAN:** ZDI-CAN-23353
- **Date:** 2024-05-29
- **CVE:** CVE-2024-4561
- **CVSS:** 4.2
- **CVSS Vector:** AV:N/AC:H/PR:L/UI:N/S:U/C:L/I:L/A:N
- **Affected Vendors:** Progress Software
- **Affected Products:** WhatsUp Gold
- **Credit:** Abdessamad Lahlali of Trend Micro.
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-517/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Progress Software WhatsUp Gold. Authentication is required to exploit this vulnerability. The specific flaw exists within the FaviconController class. The issue results from following HTTP redirects. An attacker can leverage this vulnerability to disclose information in the context of the application.

## Additional Details

Progress Software has issued an update to correct this vulnerability. More details can be found at: https://community.progress.com/s/article/Announcing-WhatsUp-Gold-v2023-1-2

## Disclosure Timeline

- 2024-02-21 - Vulnerability reported to vendor
- 2024-05-29 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
