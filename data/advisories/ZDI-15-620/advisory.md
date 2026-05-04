# ZDI-15-620: Autodesk Design Review GIF GlobalColorTable Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-620
- **ZDI-CAN:** ZDI-CAN-2844
- **Date:** 2015-12-08
- **CVE:** CVE-2015-8572
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Autodesk
- **Affected Products:** Design Review
- **Credit:** kdot
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-620/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Autodesk Design Review. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of GIF files. The issue lies in the failure to handle the case when the GlobalColorTable is present despite not being specified. An attacker could leverage this vulnerability to execute code within the context of the current process.

## Additional Details

Autodesk has issued an update to correct this vulnerability. More details can be found at: https://knowledge.autodesk.com/support/design-review/downloads/caas/downloads/content/autodesk-design-review-2013-hotfix.html

## Disclosure Timeline

- 2015-05-20 - Vulnerability reported to vendor
- 2015-12-08 - Coordinated public release of advisory
