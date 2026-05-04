# ZDI-12-186: Microsoft Office 2007 RTF Mismatch Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-186
- **ZDI-CAN:** ZDI-CAN-1402
- **Date:** 2012-11-15
- **CVE:** CVE-2012-0183
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Office
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-186/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Office. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of RTF files. The code responsible for lexing control words from the input file does not properly validate that all objects are properly defined. By removing terminating values within an RTF file an attacker can cause the program to re-use a freed object. Combined with basic memory layout control an attacker can abuse this situation to achieve code execution under the context of the user running the application.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://technet.microsoft.com/en-us/security/bulletin/ms12-029

## Disclosure Timeline

- 2011-11-29 - Vulnerability reported to vendor
- 2012-11-15 - Coordinated public release of advisory
