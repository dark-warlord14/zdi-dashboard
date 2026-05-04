# ZDI-10-132: Mozilla Firefox Plugin Parameter EnsureCachedAttrParamArrays Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-132
- **ZDI-CAN:** ZDI-CAN-821
- **Date:** 2010-07-20
- **CVE:** CVE-2010-1214
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Mozilla Firefox
- **Affected Products:** 3.6.x
- **Credit:** J23 (http://twitter.com/HansJ23)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-132/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Mozilla Firefox. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the browser's method for parsing child elements out of a particular tag. The application will use a 32-bit index to enumerate them, but will store it in a 16-bit signed integer and then use it to allocate space for a cache. When populating the cache a buffer overflow will occur. This can lead to code execution under the context of the application.

## Additional Details

Mozilla Firefox has issued an update to correct this vulnerability. More details can be found at: http://www.mozilla.org/security/announce/2010/mfsa2010-37.html

## Disclosure Timeline

- 2010-06-17 - Vulnerability reported to vendor
- 2010-07-20 - Coordinated public release of advisory
