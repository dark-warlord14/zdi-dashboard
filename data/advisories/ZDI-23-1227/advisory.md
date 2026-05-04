# ZDI-23-1227: Samba Spotlight mdssvc RPC Request Infinite Loop Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1227
- **ZDI-CAN:** ZDI-CAN-20229
- **Date:** 2023-08-25
- **CVE:** CVE-2023-34967
- **CVSS:** 5.9
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** Samba
- **Affected Products:** Samba
- **Credit:** Florent Saudel (@thalium_team)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1227/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Samba. Authentication is not required to exploit this vulnerability. The specific flaw exists within the parsing of Spotlight RPC arguments. Crafted arguments can force the server into an infinite loop. An attacker can leverage this vulnerability to create a denial-of-service condition on the service.

## Additional Details

Samba has issued an update to correct this vulnerability. More details can be found at: https://www.samba.org/samba/security/CVE-2023-34967.html

## Disclosure Timeline

- 2023-03-22 - Vulnerability reported to vendor
- 2023-08-25 - Coordinated public release of advisory
