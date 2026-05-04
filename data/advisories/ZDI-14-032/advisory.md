# ZDI-14-032: Microsoft Internet Explorer Uninitialized Variable Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-032
- **ZDI-CAN:** ZDI-CAN-2033
- **Date:** 2014-03-20
- **CVE:** CVE-2014-0299
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Jose A. Vazquez of Yenteasy - Security Research -
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-032/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of HTML tables. An uninitialized variable in one of the functions can cause memory corruption. This can lead to remote code execution under the context of the program.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/security/bulletin/MS14-012

## Disclosure Timeline

- 2013-11-21 - Vulnerability reported to vendor
- 2014-03-20 - Coordinated public release of advisory
