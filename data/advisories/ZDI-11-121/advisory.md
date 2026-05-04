# ZDI-11-121: Microsoft Office XP Data Validation Record Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-121
- **ZDI-CAN:** ZDI-CAN-912
- **Date:** 2011-04-12
- **CVE:** CVE-2011-0105
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Excel
- **Credit:** Aniway (Aniway.Anyway AT gmail DOT com)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-121/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Office Excel. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the application's parsing of a particular record within a Microsoft Excel Compound Document. When specifying a particular value, the application will fail to initialize a variable that is used as the length of a memcpy operation. Due to the usage of the uninitialized value, with proper control of the program flow an attacker can force a length of their own choosing for the memcpy operation. This will cause a buffer overflow and can lead to code execution under the context of the application.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/ms11-021.mspx

## Disclosure Timeline

- 2010-10-18 - Vulnerability reported to vendor
- 2011-04-12 - Coordinated public release of advisory
