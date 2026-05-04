# ZDI-10-131: Mozilla Firefox nsTreeSelection Dangling Pointer Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-131
- **ZDI-CAN:** ZDI-CAN-755
- **Date:** 2010-07-20
- **CVE:** CVE-2010-2753
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Mozilla Firefox
- **Affected Products:** 3.6.x
- **Credit:** regenrecht
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-131/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Mozilla Firefox. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the implementation of XUL <tree> element's "selection" attribute. There is an integer overflow when calculating the bounds of a new selection range. When calling adjustSelection on this manged range both ranges are deleted leaving a dangling reference. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the browser.

## Additional Details

Mozilla Firefox has issued an update to correct this vulnerability. More details can be found at: http://www.mozilla.org/security/announce/2010/mfsa2010-40.html

## Disclosure Timeline

- 2010-06-09 - Vulnerability reported to vendor
- 2010-07-20 - Coordinated public release of advisory
