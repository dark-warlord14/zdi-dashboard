# ZDI-22-1161: (Pwn2Own) Softing Secure Integration Server Use of Default Credentials Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1161
- **ZDI-CAN:** ZDI-CAN-17056
- **Date:** 2022-08-23
- **CVE:** CVE-2022-2336
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Softing
- **Affected Products:** Secure Integration Server
- **Credit:** Flashback Team: Pedro Ribeiro (@pedrib1337) && Radek Domanski (@RabbitPro)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1161/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Softing Secure Integration Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the default configuration of user accounts. The configuration contains hard-coded credentials. An attacker can leverage this vulnerability to bypass authentication and execute arbitrary code in the context of the Administrator.

## Additional Details

Softing has issued an update to correct this vulnerability. More details can be found at: https://industrial.softing.com/fileadmin/psirt/downloads/syt-2022-6.html

## Disclosure Timeline

- 2022-05-09 - Vulnerability reported to vendor
- 2022-08-23 - Coordinated public release of advisory
