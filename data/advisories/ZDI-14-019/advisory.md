# ZDI-14-019: Microsoft Direct2D Graphics Component Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-019
- **ZDI-CAN:** ZDI-CAN-1877
- **Date:** 2014-02-13
- **CVE:** CVE-2014-0263
- **CVSS:** 5.1
- **CVSS Vector:** AV:N/AC:H/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Omair
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-019/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of SVG path nodes. The issue lies in a miscalculation when processing a path containing overly large values. An attacker can leverage this situation to execute code under the context of the user running the browser.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/security/bulletin/MS14-007

## Disclosure Timeline

- 2013-06-10 - Vulnerability reported to vendor
- 2014-02-13 - Coordinated public release of advisory
