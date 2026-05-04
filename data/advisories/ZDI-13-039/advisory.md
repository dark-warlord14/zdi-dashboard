# ZDI-13-039: Mozilla Firefox ListenerManager Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-039
- **ZDI-CAN:** ZDI-CAN-1591
- **Date:** 2013-03-22
- **CVE:** CVE-2013-0754
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Mozilla
- **Affected Products:** Firefox
- **Credit:** regenrecht
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-039/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Mozilla Firefox. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of ListenerManager event listeners. A dangling pointer can be created if a listener frees another listener. By abusing this behavior an attacker can ensure this memory is under control and leverage the situation to achieve remote code execution under the context of the user running the browser.

## Additional Details

Mozilla has issued an update to correct this vulnerability. More details can be found at: http://www.mozilla.org/security/announce/2013/mfsa2013-17.html

## Disclosure Timeline

- 2012-11-21 - Vulnerability reported to vendor
- 2013-03-22 - Coordinated public release of advisory
