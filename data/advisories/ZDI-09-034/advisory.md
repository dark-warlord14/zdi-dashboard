# ZDI-09-034: Apple Safari SVG Set.targetElement() Memory Corruption Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-034
- **ZDI-CAN:** ZDI-CAN-401
- **Date:** 2009-06-08
- **CVE:** CVE-2009-1709
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-034/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists in the garbage collection of JavaScript set elements in WebCore. When an SVG set object is appended to an SVG marker element that is dereferenced, calls to the targetElement attribute will fail to reference count the marker element. When the set element is appended to another object, subsequent calls to the targetElement attribute will result in a heap corruption which can be leveraged to execute arbitrary code under the context of the current user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT3613

## Disclosure Timeline

- 2008-11-10 - Vulnerability reported to vendor
- 2009-06-08 - Coordinated public release of advisory
