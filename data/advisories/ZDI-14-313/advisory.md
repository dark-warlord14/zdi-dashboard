# ZDI-14-313: Microsoft Internet Explorer CSelectTracker::GetMoveDirection Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-313
- **ZDI-CAN:** ZDI-CAN-2392
- **Date:** 2014-09-16
- **CVE:** CVE-2014-4105
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Yuki Chen
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-313/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The vulnerability relates to how Internet Explorer handles selections within a document. By manipulating elements within the document and well as changing the current selection, an attacker can force a CDisplayPointer object in memory to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/MS14-052

## Disclosure Timeline

- 2014-06-30 - Vulnerability reported to vendor
- 2014-09-16 - Coordinated public release of advisory
