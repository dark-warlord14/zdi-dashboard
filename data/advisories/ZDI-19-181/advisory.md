# ZDI-19-181: Microsoft SharePoint EntityInstanceIdEncoder Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-181
- **ZDI-CAN:** ZDI-CAN-7262
- **Date:** 2019-02-12
- **CVE:** CVE-2019-0604
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** SharePoint
- **Credit:** Markus Wulftange (@mwulftange)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-181/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft SharePoint. Authentication is required to exploit this vulnerability. The specific flaw exists within the EntityInstanceIdEncoder class. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of Administrator.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-0604

## Disclosure Timeline

- 2018-09-23 - Vulnerability reported to vendor
- 2019-02-12 - Coordinated public release of advisory
- 2019-12-18 - Advisory Updated
