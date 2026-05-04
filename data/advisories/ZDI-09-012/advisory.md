# ZDI-09-012: Microsoft Internet Explorer Malformed CSS Memory Corruption Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-012
- **ZDI-CAN:** ZDI-CAN-400
- **Date:** 2009-02-10
- **CVE:** CVE-2009-0076
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Sam Thomas of eshu.co.uk
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-012/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists when processing, in XHTML strict mode, a CSS stylesheet containing a specific combination of style directives one of which must be a 'zoom'. The fault in processing results in a memory corruption vulnerability which can be leveraged to execute arbitrary code under the context of the current user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/MS09-002.mspx

## Disclosure Timeline

- 2008-10-15 - Vulnerability reported to vendor
- 2009-02-10 - Coordinated public release of advisory
