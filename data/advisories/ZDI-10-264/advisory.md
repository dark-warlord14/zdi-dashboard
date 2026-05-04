# ZDI-10-264: Mozilla Firefox nsDOMAttribute MutationObserver Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-264
- **ZDI-CAN:** ZDI-CAN-898
- **Date:** 2010-12-09
- **CVE:** CVE-2010-3766
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Mozilla Firefox
- **Affected Products:** 3.6.x
- **Credit:** regenrecht
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-264/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Mozilla Firefox. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the application's support of the NodeIterator API used for element traversal. Due to a particular element not implementing functionality required by the API, a use-after free vulnerability can be forced to occur. This can be used to achieve code execution under the context of the application.

## Additional Details

Mozilla Firefox has issued an update to correct this vulnerability. More details can be found at: http://www.mozilla.org/security/announce/2010/mfsa2010-80.html

## Disclosure Timeline

- 2010-08-25 - Vulnerability reported to vendor
- 2010-12-09 - Coordinated public release of advisory
