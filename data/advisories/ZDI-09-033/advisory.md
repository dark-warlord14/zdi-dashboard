# ZDI-09-033: Apple WebKit dir Attribute Freeing Dangling Object Pointer Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-033
- **ZDI-CAN:** ZDI-CAN-430
- **Date:** 2009-06-08
- **CVE:** CVE-2009-1701
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** wushi&ling of team509
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-033/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable software utilizing the Apple WebKit library. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists when the document.body element contains a specific XML container containing various elements supporting the 'dir' attribute. During the destruction of this element, if the rendering object responsible for the element is being removed, the application will then make a call to a method for an object that doesn't exist which can lead to code execution under the context of the current user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT3613

## Disclosure Timeline

- 2009-02-09 - Vulnerability reported to vendor
- 2009-06-08 - Coordinated public release of advisory
