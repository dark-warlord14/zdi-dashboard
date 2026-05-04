# ZDI-12-110: Mozilla Firefox AttributeChildRemoved Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-110
- **ZDI-CAN:** ZDI-CAN-1413
- **Date:** 2012-06-28
- **CVE:** CVE-2011-3659
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Mozilla
- **Affected Products:** Firefox
- **Credit:** regenrecht
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-110/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Mozilla Firefox. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the way Firefox handles nsDOMAttribute child removal. It is possible to remove a child without setting the removed child pointer to NULL, thus leaving it still accessible as a dangling pointer. Subsequent use of this pointer allows for remote code execution.

## Additional Details

Mozilla has issued an update to correct this vulnerability. More details can be found at: http://www.mozilla.org/security/announce/2012/mfsa2012-04.html

## Disclosure Timeline

- 2011-12-01 - Vulnerability reported to vendor
- 2012-06-28 - Coordinated public release of advisory
