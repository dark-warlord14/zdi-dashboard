# ZDI-13-231: Microsoft Internet Explorer CTreePos Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-231
- **ZDI-CAN:** ZDI-CAN-1925
- **Date:** 2013-09-11
- **CVE:** CVE-2013-3846
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** AMol NAik
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-231/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within an object created by CSpliceTreeEngine::InsertSplice. The process can be forced to reuse a dangling pointer of the object resulting in a use-after-free condition. An attacker can leverage this situation to execute code under the context of the user running the browser.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/security/bulletin/ms13-055

## Disclosure Timeline

- 2013-06-28 - Vulnerability reported to vendor
- 2013-09-11 - Coordinated public release of advisory
