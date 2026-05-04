# ZDI-09-048: Microsoft Internet Explorer CSS Behavior Memory Corruption Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-048
- **ZDI-CAN:** ZDI-CAN-484
- **Date:** 2009-08-05
- **CVE:** CVE-2009-1919
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Peter Vreugdenhil
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-048/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists when accessing embedded style sheets within an HTML file. When modifying the properties of rules defined in the style the behavior element is improperly processed resulting in a memory corruption which can be further leveraged to execute arbitrary code under the context of the current user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/Bulletin/MS09-034.mspx

## Disclosure Timeline

- 2009-04-28 - Vulnerability reported to vendor
- 2009-08-05 - Coordinated public release of advisory
