# ZDI-09-013: Mozilla Firefox XUL Linked Clones Double Free Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-013
- **ZDI-CAN:** ZDI-CAN-423
- **Date:** 2009-03-05
- **CVE:** CVE-2009-0775
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Mozilla Firefox
- **Affected Products:** 3.0.x
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-013/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Mozilla Firefox. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists during the browsers garbage collection process. When multiple DOM elements are cloned and linked to one another and the browser is reloaded, a memory corruption occurs resulting in a double free. This can be leveraged to execute arbitrary code under the context of the current user.

## Additional Details

Mozilla Firefox has issued an update to correct this vulnerability. More details can be found at: http://www.mozilla.org/security/announce/2009/mfsa2009-08.html

## Disclosure Timeline

- 2009-01-19 - Vulnerability reported to vendor
- 2009-03-05 - Coordinated public release of advisory
