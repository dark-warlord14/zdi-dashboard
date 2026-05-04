# ZDI-11-124: Microsoft PowerPoint TimeColorBehaviorContainer Floating Point Record Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-124
- **ZDI-CAN:** ZDI-CAN-902
- **Date:** 2011-04-12
- **CVE:** CVE-2011-0655
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Office PowerPoint
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-124/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Office PowerPoint. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within how the application parses a record associated with animation. If a container holds a specific record type, the application will explicitly trust a length used in this record to calculate a pointer for copying floating point numbers to. This can be used to write outside of an allocated buffer and will lead to code execution under the context of the application.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/Bulletin/MS11-022.mspx

## Disclosure Timeline

- 2010-09-14 - Vulnerability reported to vendor
- 2011-04-12 - Coordinated public release of advisory
