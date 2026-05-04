# ZDI-08-040: Microsoft DirectX SAMI File Format Name Parsing Stack Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-040
- **ZDI-CAN:** ZDI-CAN-281
- **Date:** 2008-06-10
- **CVE:** CVE-2008-1444
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows 2000 SP4
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-040/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists in the parsing of SAMI files. When handling the properties of a "Class Name" variable a lack of bounds checking can result in a stack overflow. Successful exploitation can lead to remote code execution under the credentials of the logged in user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/Bulletin/MS08-033.mspx

## Disclosure Timeline

- 2008-01-21 - Vulnerability reported to vendor
- 2008-06-10 - Coordinated public release of advisory
