# ZDI-12-113: IBM Rational ClearQuest CQOle ActiveX Control Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-113
- **ZDI-CAN:** ZDI-CAN-1249
- **Date:** 2012-06-28
- **CVE:** CVE-2012-0708
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** IBM
- **Affected Products:** Rational ClearQuest
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-113/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of IBM Rational ClearQuest. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the CQOle ActiveX control. A function prototype mismatch in an ActiveX wrapper results in an extra argument to be pushed onto the stack, thereby misaligning the stack offset. When the function returns, it can be made to jump to a memory address provided via the ActiveX method call. This can be leveraged to execute arbitrary code under the context of the user running the browser.

## Additional Details

IBM has issued an update to correct this vulnerability. More details can be found at: http://www-304.ibm.com/support/docview.wss?uid=swg21591705

## Disclosure Timeline

- 2011-11-29 - Vulnerability reported to vendor
- 2012-06-28 - Coordinated public release of advisory
