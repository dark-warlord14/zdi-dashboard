# ZDI-16-667: Autodesk Design Review BMP Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-667
- **ZDI-CAN:** ZDI-CAN-3573
- **Date:** 2016-12-15
- **CVE:** N/A
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Autodesk
- **Affected Products:** Design Review
- **Credit:** Mario Gomes(@NetFuzzer)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-667/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Autodesk Design Review. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of BMP files. The issue lies in the failure to validate the size of the biClrUsed field prior to copying data into a fixed-size stack buffer. An attacker can leverage this vulnerability to execute code within the context of the current process.

## Additional Details

Autodesk has issued an update to correct this vulnerability. More details can be found at: https://knowledge.autodesk.com/support/design-review/downloads/caas/downloads/content/autodesk-design-review-2013-hotfix.html?v=2013

## Disclosure Timeline

- 2016-11-09 - Vulnerability reported to vendor
- 2016-12-15 - Coordinated public release of advisory
