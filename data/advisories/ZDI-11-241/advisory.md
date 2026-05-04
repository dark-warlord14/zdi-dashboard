# ZDI-11-241: Webkit setAttributes attributeChanged Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-241
- **ZDI-CAN:** ZDI-CAN-1166
- **Date:** 2011-07-27
- **CVE:** CVE-2011-0254
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** WebKit
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-241/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of the Webkit Library. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the NamedNodeMap::setAttributes method defined within the NamedNodeMap.cpp file distributed with WebKit. The code responsible for copying attributes between DOM nodes does not verify that a mutation may have occurred when an attribute's attributeChanged method is called. By crafting a page that deletes instances of that attribute when the above mentioned method is called the code within setAttributes can be made to operate on freed objects. An attacker can take advantage of this by spraying the heap in a way that will not result in null pointers being referenced. This can lead to arbitrary code execution under the context of the user running the browser.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/kb/HT4808

## Disclosure Timeline

- 2011-04-19 - Vulnerability reported to vendor
- 2011-07-27 - Coordinated public release of advisory
- 2020-07-30 - Advisory Updated
