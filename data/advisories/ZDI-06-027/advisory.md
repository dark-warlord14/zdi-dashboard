# ZDI-06-027: Microsoft Internet Explorer CSS Class Ordering Memory Corruption Vulnerability

## Metadata

- **ZDI ID:** ZDI-06-027
- **ZDI-CAN:** ZDI-CAN-066
- **Date:** 2006-08-08
- **CVE:** CVE-2006-3450
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Sam Thomas
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-06-027/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific vulnerability exists due to improper handling of CSS class values. Accessing a specially crafted CSS element via document.getElementByID causes a memory corruption eventually leading to code execution.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/MS06-042.mspx

## Disclosure Timeline

- 2006-06-14 - Vulnerability reported to vendor
- 2006-08-08 - Coordinated public release of advisory
