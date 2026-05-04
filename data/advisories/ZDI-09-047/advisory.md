# ZDI-09-047: Microsoft Internet Explorer getElementsByTagName Memory Corruption Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-047
- **ZDI-CAN:** ZDI-CAN-483
- **Date:** 2009-08-05
- **CVE:** CVE-2009-1918
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** wushi&ling of team509
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-047/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists in the appending of elements to an invalid object. When appending malformed elements to a empty DIV element memory corruption can occur. A properly constructed web page can result in remote code execution under the context of the current user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/Bulletin/MS09-034.mspx

## Disclosure Timeline

- 2009-04-28 - Vulnerability reported to vendor
- 2009-08-05 - Coordinated public release of advisory
