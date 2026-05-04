# ZDI-07-073: Microsoft Internet Explorer setExpression Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-073
- **ZDI-CAN:** ZDI-CAN-229
- **Date:** 2007-12-11
- **CVE:** CVE-2007-3902
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-073/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists in the CRecalcProperty function in mshtml.dll. When rendering HTML after calling the setExpression methods, followed by a modification of the outerHTML property of a programatically created element. The vulnerable code dereferences a previously freed memory location which can be leveraged to execute arbitrary code.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/ms07-069.mspx

## Disclosure Timeline

- 2007-07-20 - Vulnerability reported to vendor
- 2007-12-11 - Coordinated public release of advisory
- 2020-04-17 - Advisory Updated
