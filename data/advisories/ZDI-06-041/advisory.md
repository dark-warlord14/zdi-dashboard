# ZDI-06-041: Microsoft Internet Explorer CSS Float Property Memory Corruption Vulnerability

## Metadata

- **ZDI ID:** ZDI-06-041
- **ZDI-CAN:** ZDI-CAN-080
- **Date:** 2006-11-14
- **CVE:** CVE-2006-4687
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Sam Thomas
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-06-041/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific vulnerability exists due to improper parsing of HTML CSS 'float' properties. By ordering specially crafted 'div' tags in a web page, memory corruption can occur leading to remote code execution.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/Bulletin/MS06-067.mspx

## Disclosure Timeline

- 2006-07-18 - Vulnerability reported to vendor
- 2006-11-14 - Coordinated public release of advisory
