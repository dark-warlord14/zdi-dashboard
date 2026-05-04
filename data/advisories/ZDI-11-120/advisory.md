# ZDI-11-120: Microsoft Office Excel RealTimeData Record Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-120
- **ZDI-CAN:** ZDI-CAN-1007
- **Date:** 2011-04-12
- **CVE:** CVE-2011-0101
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Excel 2002
- **Credit:** Aniway (Aniway.Anyway AT gmail DOT com)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-120/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Office Excel. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The flaw exists within the methods used for RealTimeData Record Parsing. When handling a stTopic field has a bit set specifying double byte characters in the following field the value of a global pointer is improperly calculated. This pointer is later used in a memcpy operation whose source is user supplied data. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/ms11-021.mspx

## Disclosure Timeline

- 2010-11-15 - Vulnerability reported to vendor
- 2011-04-12 - Coordinated public release of advisory
