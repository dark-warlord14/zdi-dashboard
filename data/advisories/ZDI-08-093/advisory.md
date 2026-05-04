# ZDI-08-093: Mozilla Firefox Input Box Type Property Dangling Pointer Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-093
- **ZDI-CAN:** ZDI-CAN-390
- **Date:** 2008-11-12
- **CVE:** CVE-2008-5021
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Mozilla Firefox, Mozilla Firefox
- **Affected Products:** 3.0.x, 2.0.x
- **Credit:** ling and wushi of team509
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-093/
## Vulnerability Details

This vulnerability allows attackers to potentially execute arbitrary code on vulnerable installations of Mozilla Firefox. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists when a DOM method on a specific HTML form object is called before the object itself has actually completed it's initialization. This will lead to a call of uninitialized data which can result in code execution under the context of the current user.

## Additional Details

Mozilla Firefox has issued an update to correct this vulnerability. More details can be found at: http://www.mozilla.org/security/announce/2008/mfsa2008-55.html

## Disclosure Timeline

- 2008-09-23 - Vulnerability reported to vendor
- 2008-11-12 - Coordinated public release of advisory
