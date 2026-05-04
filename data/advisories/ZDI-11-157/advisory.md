# ZDI-11-157: Mozilla Firefox nsTreeRange Dangling Pointer Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-157
- **ZDI-CAN:** ZDI-CAN-1084
- **Date:** 2011-05-09
- **CVE:** CVE-2011-0073
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Mozilla
- **Affected Products:** Firefox
- **Credit:** regenrecht
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-157/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Mozilla Firefox. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the way Firefox handles user defined functions of a nsTreeSelection element. When executing the function invalidateSelection it is possible to free the nsTreeSelection object that the function operates on. Any further operations on the freed object can result in remote code execution.

## Additional Details

Mozilla has issued an update to correct this vulnerability. More details can be found at: http://www.mozilla.org/security/announce/2011/mfsa2011-13.html

## Disclosure Timeline

- 2011-02-02 - Vulnerability reported to vendor
- 2011-05-09 - Coordinated public release of advisory
