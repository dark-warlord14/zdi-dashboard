# ZDI-14-261: Microsoft Internet Explorer CAttrValue Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-261
- **ZDI-CAN:** ZDI-CAN-2366
- **Date:** 2014-07-23
- **CVE:** CVE-2014-1765
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** 0016EECD9D7159A949DAD3BC17E0A939
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-261/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of CAttrValue objects. An uninitialized variable in one of the functions can cause memory corruption. This can lead to remote code execution under the context of the program.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/ms14-035

## Disclosure Timeline

- 2014-06-09 - Vulnerability reported to vendor
- 2014-07-23 - Coordinated public release of advisory
