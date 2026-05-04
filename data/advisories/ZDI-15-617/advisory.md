# ZDI-15-617: Autodesk Design Review BMP biClrUsed Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-617
- **ZDI-CAN:** ZDI-CAN-2925
- **Date:** 2015-12-08
- **CVE:** CVE-2015-8571
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Autodesk
- **Affected Products:** Design Review
- **Credit:** kdot
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-617/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Autodesk Design Review. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of BMP files. The issue lies in the the failure to test for an integer overflow when multiplying the biClrUsed value by four. An attacker could leverage this vulnerability to execute code within the context of the current process.

## Additional Details

Autodesk has issued an update to correct this vulnerability. More details can be found at: https://knowledge.autodesk.com/support/design-review/downloads/caas/downloads/content/autodesk-design-review-2013-hotfix.html

## Disclosure Timeline

- 2015-05-20 - Vulnerability reported to vendor
- 2015-12-08 - Coordinated public release of advisory
