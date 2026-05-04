# ZDI-08-006: Microsoft Internet Explorer SVG animateMotion.by Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-006
- **ZDI-CAN:** ZDI-CAN-243
- **Date:** 2008-02-12
- **CVE:** CVE-2008-0077
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-006/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists in the handling of the "by" property of an animateMotion SVG element. By assigning other DOM elements to this property, a memory corruption occurs during the destruction of a Variant data type. The corruption causes an overwrite of a virtual function address allowing for the execution of arbitrary code.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/Bulletin/MS08-010.mspx

## Disclosure Timeline

- 2007-09-17 - Vulnerability reported to vendor
- 2008-02-12 - Coordinated public release of advisory
