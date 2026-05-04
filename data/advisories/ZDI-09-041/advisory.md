# ZDI-09-041: Microsoft Internet Explorer 8 Rows Property Dangling Pointer Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-041
- **ZDI-CAN:** ZDI-CAN-463
- **Date:** 2009-06-10
- **CVE:** CVE-2009-1532
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Nils
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-041/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer 8. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists during the rendering of an HTML page with malformed row property references, resulting in a dangling pointer which can be abused to execute arbitrary code. Internet Explorer 7 is not affected.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/MS09-019.mspx

## Disclosure Timeline

- 2009-03-19 - Vulnerability reported to vendor
- 2009-06-10 - Coordinated public release of advisory
