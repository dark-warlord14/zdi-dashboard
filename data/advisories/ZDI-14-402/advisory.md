# ZDI-14-402: Autodesk Design Review AdView.AdViewer.1 Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-402
- **ZDI-CAN:** ZDI-CAN-2197
- **Date:** 2014-12-04
- **CVE:** CVE-2014-9268
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Autodesk
- **Affected Products:** Design Review
- **Credit:** Andrea Micalizzi (rgod)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-402/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Autodesk Design Review. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the AdView.AdViewer.1 ActiveX control. By providing a malformed DWF file to the control, an attacker can execute arbitrary code in the context of the browser.

## Additional Details

Autodesk has issued an update to correct this vulnerability. More details can be found at: http://knowledge.autodesk.com/support/design-review/downloads/caas/downloads/content/autodesk-design-review-2013-hotfix.html

## Disclosure Timeline

- 2014-05-12 - Vulnerability reported to vendor
- 2014-12-04 - Coordinated public release of advisory
