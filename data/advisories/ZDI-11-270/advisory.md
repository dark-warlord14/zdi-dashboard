# ZDI-11-270: Mozilla Firefox SVGTextElement.getCharNumAtPosition Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-270
- **ZDI-CAN:** ZDI-CAN-1143
- **Date:** 2011-08-17
- **CVE:** CVE-2011-0084
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Mozilla
- **Affected Products:** Firefox
- **Credit:** regenrecht
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-270/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Mozilla Firefox. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the code responsible for parsing SVG text containers. The code within nsSVGGlyphFrame::GetCharNumAtPosition() does not account for user defined getter methods modifying or destroying the parent object. An attacker can abuse this flaw to create a dangling pointer which is referenced during the traversal of the SVG container hierarchy. This can be leveraged to execute arbitrary code within the context of the browser.

## Additional Details

Mozilla has issued an update to correct this vulnerability. More details can be found at: http://www.mozilla.org/security/announce/2011/mfsa2011-30.html#cve-2011-0084

## Disclosure Timeline

- 2011-04-04 - Vulnerability reported to vendor
- 2011-08-17 - Coordinated public release of advisory
