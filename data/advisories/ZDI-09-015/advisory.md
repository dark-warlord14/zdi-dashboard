# ZDI-09-015: Mozilla Firefox XUL _moveToEdgeShift() Memory Corruption Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-015
- **ZDI-CAN:** ZDI-CAN-465
- **Date:** 2009-03-30
- **CVE:** CVE-2009-1044
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Mozilla Firefox
- **Affected Products:** 3.0.x
- **Credit:** Nils
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-015/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Mozilla Firefox. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists in the XUL tree method _moveToEdgeShift(). In some cases this call will trigger garbage collection routines on in use objects which will result in a future call to a dangling pointer. This can be leveraged to execute arbitrary code under the context of the current user.

## Additional Details

Mozilla Firefox has issued an update to correct this vulnerability. More details can be found at: http://www.mozilla.org/security/announce/2009/mfsa2009-13.html

## Disclosure Timeline

- 2009-03-19 - Vulnerability reported to vendor
- 2009-03-30 - Coordinated public release of advisory
