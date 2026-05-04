# ZDI-11-103: Mozilla Firefox JSON.stringify Dangling Pointer Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-103
- **ZDI-CAN:** ZDI-CAN-971
- **Date:** 2011-03-02
- **CVE:** CVE-2011-0055
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Mozilla
- **Affected Products:** Firefox
- **Credit:** regenrecht
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-103/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Firefox. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within js3250.dll. In the JSON.stringify() call chain js_HasOwnProperty() is called with an invalid pointer. The pointer becomes invalid due to being unrooted and garbage collection occurring. Dereferecing of this pointer allows a remote attacker to execute arbitrary code in the context of the user running the browser.

## Additional Details

Mozilla has issued an update to correct this vulnerability. More details can be found at: http://www.mozilla.org/security/announce/2011/mfsa2011-03.html

## Disclosure Timeline

- 2010-12-01 - Vulnerability reported to vendor
- 2011-03-02 - Coordinated public release of advisory
