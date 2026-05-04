# ZDI-10-011: Microsoft Internet Explorer Table Layout Col Tag Cache Update Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-011
- **ZDI-CAN:** ZDI-CAN-501
- **Date:** 2010-01-21
- **CVE:** CVE-2010-0244
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** wushi of team509
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-011/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists when a Col element is used within an HTML table container. If this element is removed while the table is in use a cache that exists of the table's cells will be used after one of it's elements has been invalidated. This can lead to code execution under the context of the currently logged in user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/ms10-002.mspx

## Disclosure Timeline

- 2009-07-14 - Vulnerability reported to vendor
- 2010-01-21 - Coordinated public release of advisory
