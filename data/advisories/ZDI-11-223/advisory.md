# ZDI-11-223: Mozilla Firefox SVGPathSegList.replaceItem Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-223
- **ZDI-CAN:** ZDI-CAN-1142
- **Date:** 2011-06-21
- **CVE:** CVE-2011-0083
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Mozilla
- **Affected Products:** Firefox
- **Credit:** regenrecht
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-223/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Mozilla Firefox. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the code responsible for parsing SVG path segment objects. The function nsSVGPathSegList::ReplaceItem() does not account for deletion of the segment object list within a user defined DOMAttrModified EventListener. Code within nsSVGPathSegList::ReplaceItem() references the segment list without verifying that it was not deleted in the aforementioned callback. This can be abused to create a dangling reference which can be leveraged to execute arbitrary code within the context of the browser.

## Additional Details

Mozilla has issued an update to correct this vulnerability. More details can be found at: http://www.mozilla.org/security/announce/2011/mfsa2011-23.html

## Disclosure Timeline

- 2011-04-04 - Vulnerability reported to vendor
- 2011-06-21 - Coordinated public release of advisory
