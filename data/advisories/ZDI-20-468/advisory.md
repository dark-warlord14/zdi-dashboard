# ZDI-20-468: Microsoft SharePoint TypeConverter Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-468
- **ZDI-CAN:** ZDI-CAN-10027
- **Date:** 2020-04-15
- **CVE:** CVE-2020-0932
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** SharePoint
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-468/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft SharePoint Server. Authentication is required to exploit this vulnerability. The specific flaw exists within the use of TypeConverter classes. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of the SharePoint service at high integrity.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-0932

## Disclosure Timeline

- 2020-02-07 - Vulnerability reported to vendor
- 2020-04-15 - Coordinated public release of advisory
- 2020-10-27 - Advisory Updated
