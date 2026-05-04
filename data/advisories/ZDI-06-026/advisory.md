# ZDI-06-026: Microsoft Internet Explorer Multiple CSS Imports Memory Corruption Vulnerability

## Metadata

- **ZDI ID:** ZDI-06-026
- **ZDI-CAN:** ZDI-CAN-058
- **Date:** 2006-08-08
- **CVE:** CVE-2006-3451
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Sam Thomas
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-06-026/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists due to improper garbage collection when multiple "imports" are used on a "styleSheets" collection. Crafting a long chain of CSS imports in an HTML document results in a memory corruption eventually leading to code execution.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/MS06-042.mspx

## Disclosure Timeline

- 2006-06-14 - Vulnerability reported to vendor
- 2006-08-08 - Coordinated public release of advisory
