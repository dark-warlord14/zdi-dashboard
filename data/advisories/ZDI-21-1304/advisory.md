# ZDI-21-1304: Orckestra C1 CMS Composite Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1304
- **ZDI-CAN:** ZDI-CAN-14740
- **Date:** 2021-11-11
- **CVE:** CVE-2021-34992
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Orckestra
- **Affected Products:** C1 CMS
- **Credit:** Le Ngoc Anh - Sun* Cyber Security Research Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1304/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Orckestra C1 CMS. Authentication is required to exploit this vulnerability. The specific flaw exists within Composite.dll. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

Orckestra has issued an update to correct this vulnerability. More details can be found at: https://github.com/Orckestra/C1-CMS-Foundation/releases/tag/v6.11

## Disclosure Timeline

- 2021-10-25 - Vulnerability reported to vendor
- 2021-11-11 - Coordinated public release of advisory
