# ZDI-15-619: Autodesk Design Review GIF DataSubBlock Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-619
- **ZDI-CAN:** ZDI-CAN-2762
- **Date:** 2015-12-08
- **CVE:** CVE-2015-8572
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Autodesk
- **Affected Products:** Design Review
- **Credit:** kdot
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-619/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Autodesk Design Review. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of GIF files. The issue lies in the failure to ensure that the DataSubBlock sizes are valid. An attacker could leverage this vulnerability to execute code within the context of the current process.

## Additional Details

Autodesk has issued an update to correct this vulnerability. More details can be found at: https://knowledge.autodesk.com/support/design-review/downloads/caas/downloads/content/autodesk-design-review-2013-hotfix.html

## Disclosure Timeline

- 2015-05-20 - Vulnerability reported to vendor
- 2015-12-08 - Coordinated public release of advisory
