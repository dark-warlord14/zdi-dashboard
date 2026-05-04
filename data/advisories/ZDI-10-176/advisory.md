# ZDI-10-176: Mozilla Firefox normalizeDocument Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-176
- **ZDI-CAN:** ZDI-CAN-866
- **Date:** 2010-09-13
- **CVE:** CVE-2010-2766
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Mozilla Firefox
- **Affected Products:** 3.6.x
- **Credit:** regenrecht
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-176/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Mozilla Firefox. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The flaw exists within the normalizeDocument function defined within nsDocument.cpp. When handling children nodes the code does not account for a varying number of children during normalization. An attacker can abuse this problem along with the fact that the code does not validate the child index is within bounds to access an invalid object and execute arbitrary code under the context of the browser.

## Additional Details

Mozilla Firefox has issued an update to correct this vulnerability. More details can be found at: http://www.mozilla.org/security/announce/2010/mfsa2010-55.html

## Disclosure Timeline

- 2010-07-20 - Vulnerability reported to vendor
- 2010-09-13 - Coordinated public release of advisory
