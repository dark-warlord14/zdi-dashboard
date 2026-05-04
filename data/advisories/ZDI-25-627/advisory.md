# ZDI-25-627: rocket.chat Incorrect Authorization Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-627
- **ZDI-CAN:** ZDI-CAN-26517
- **Date:** 2025-07-21
- **CVE:** CVE-2025-7974
- **CVSS:** 3.7
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:N/A:N
- **Affected Vendors:** rocket.chat
- **Affected Products:** rocket.chat
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-627/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of rocket.chat. Authentication is not required to exploit this vulnerability. The specific flaw exists within the web service, which listens on TCP port 3000 by default. The issue results from incorrect authorization. An attacker can leverage this vulnerability to disclose information in the context of the application.

## Additional Details

Fixed in versions 7.8.0, 7.7.2, 7.6.4, 7.5.3, 7.4.4, and 7.3.6. https://github.com/RocketChat/Rocket.Chat/pull/36224

## Disclosure Timeline

- 2025-04-14 - Vulnerability reported to vendor
- 2025-07-21 - Coordinated public release of advisory
- 2025-07-21 - Advisory Updated
