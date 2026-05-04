# ZDI-08-045: Apple Safari StyleSheet ownerNode Heap Corruption Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-045
- **ZDI-CAN:** ZDI-CAN-332
- **Date:** 2008-07-25
- **CVE:** CVE-2008-2317
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-045/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists in the garbage collection of JavaScript document elements in WebCore. When a CSSStyleSheet object of a style element is copied, and the style element is deallocated, a reference to the ownerNode property of the copied CSSStyleSheet object will result in a heap corruption allowing for the execution of arbitrary code.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT2351

## Disclosure Timeline

- 2008-05-13 - Vulnerability reported to vendor
- 2008-07-25 - Coordinated public release of advisory
