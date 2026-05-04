# ZDI-22-1122: ManageEngine OpManager Plus getUserAPIKey Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1122
- **ZDI-CAN:** ZDI-CAN-18088
- **Date:** 2022-08-18
- **CVE:** CVE-2022-36923
- **CVSS:** 9.4
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:L
- **Affected Vendors:** ManageEngine
- **Affected Products:** OpManager
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1122/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of ManageEngine OpManager Plus. Authentication is not required to exploit this vulnerability. The specific flaw exists within the getUserAPIKey function. The issue results from the lack of authentication prior to allowing access to functionality. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

ManageEngine has issued an update to correct this vulnerability. More details can be found at: https://www.manageengine.com/itom/advisory/cve-2022-36923.html

## Disclosure Timeline

- 2022-08-03 - Vulnerability reported to vendor
- 2022-08-18 - Coordinated public release of advisory
