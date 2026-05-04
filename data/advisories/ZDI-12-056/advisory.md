# ZDI-12-056: Mozilla Firefox nsSVGValue Out-of-Bounds Access Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-056
- **ZDI-CAN:** ZDI-CAN-1414
- **Date:** 2012-04-09
- **CVE:** CVE-2011-3658
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Mozilla
- **Affected Products:** Firefox
- **Credit:** regenrecht
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-056/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Mozilla Firefox. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of nsSVGValue observers. A certain method call can be made to loop excessively causing an out-of-bounds memory access. By abusing this behavior an attacker can ensure this memory is under control and leverage the situation to achieve remote code execution under the context of the user running the browser.

## Additional Details

Mozilla has issued an update to correct this vulnerability. More details can be found at: http://www.mozilla.org/security/announce/2011/mfsa2011-55.html

## Disclosure Timeline

- 2011-12-01 - Vulnerability reported to vendor
- 2012-04-09 - Coordinated public release of advisory
