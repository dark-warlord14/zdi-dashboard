# ZDI-09-056: Microsoft Office OWC10.Spreadsheet ActiveX BorderAround() Heap Corruption Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-056
- **ZDI-CAN:** ZDI-CAN-273
- **Date:** 2009-08-11
- **CVE:** CVE-2009-2496
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft, Microsoft
- **Affected Products:** Office Word, Office Excel
- **Credit:** Peter Vreugdenhil
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-056/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Microsoft Office. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific vulnerability exists in the OWC10.Spreadsheet.10 ActiveX control installed by Microsoft Office. By accessing specific methods in a certain order heap corruption occurs leading to remote code execution. If exploited, complete control of the affected system can be achieved under the rights of the currently logged in user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/MS09-043.mspx

## Disclosure Timeline

- 2007-12-11 - Vulnerability reported to vendor
- 2009-08-11 - Coordinated public release of advisory
