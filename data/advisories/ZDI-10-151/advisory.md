# ZDI-10-151: Microsoft Office Word 2007 plcffldMom Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-151
- **ZDI-CAN:** ZDI-CAN-740
- **Date:** 2010-08-11
- **CVE:** CVE-2010-1903
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Word
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-151/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Word. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the code responsible for parsing the plcffldMom structure within .doc files. By crafting malicious values within this structure an attacker can force the program to make faulty heap memory allocations. This can be leveraged to execute remote code under the context of the user running the application.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/ms10-056.mspx

## Disclosure Timeline

- 2010-06-02 - Vulnerability reported to vendor
- 2010-08-11 - Coordinated public release of advisory
