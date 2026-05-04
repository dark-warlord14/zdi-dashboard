# ZDI-12-201: Microsoft Office Word PAPX Section Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-201
- **ZDI-CAN:** ZDI-CAN-1281
- **Date:** 2012-12-21
- **CVE:** CVE-2012-0182
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Word
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-201/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Office Word. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within how the application parses a PAPX FKP sections. When parsing a PAPX FKP section, the application will store a calculation. However, when repairing a damaged document, the application will explicitly trust this calculation in a loop that is used to index into an array of objects. This will allow for an out-of-bounds access of an object which can lead to code execution under the context of the application.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://technet.microsoft.com/en-us/security/bulletin/ms12-064

## Disclosure Timeline

- 2011-05-25 - Vulnerability reported to vendor
- 2012-12-21 - Coordinated public release of advisory
