# ZDI-15-247: Microsoft Internet Explorer hr Element Uninitialized Variable Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-247
- **ZDI-CAN:** ZDI-CAN-2764
- **Date:** 2015-06-11
- **CVE:** CVE-2015-1735
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Zheng Huang of Baidu Scloud XTeam
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-247/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The vulnerability relates to how Internet Explorer processes certain operations on HTML hr elements. Internet Explorer erroneously uses a VARIANT structure in memory before it has been properly initialized. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS15-056

## Disclosure Timeline

- 2015-02-20 - Vulnerability reported to vendor
- 2015-06-11 - Coordinated public release of advisory
