# ZDI-22-1418: Adobe ColdFusion Admin Component Use of Hard-coded Credentials Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1418
- **ZDI-CAN:** ZDI-CAN-16921
- **Date:** 2022-10-14
- **CVE:** CVE-2022-38420
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** ColdFusion
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1418/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Adobe ColdFusion. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Admin Component service. The service uses a hard-coded password for the administrator user. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/coldfusion/apsb22-44.html

## Disclosure Timeline

- 2022-05-13 - Vulnerability reported to vendor
- 2022-10-14 - Coordinated public release of advisory
