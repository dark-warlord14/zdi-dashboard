# ZDI-13-146: Microsoft Internet Explorer CTreeNode Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-146
- **ZDI-CAN:** ZDI-CAN-1781
- **Date:** 2013-06-27
- **CVE:** CVE-2013-3141
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-146/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of CTreeNode objects. Specifically crafted DOM manipulations can be used to cause a use-after-free condition on the CTreeNode object. An attacker may be able to leverage this situation to execute code under the context of the user running the browser.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://technet.microsoft.com/en-us/security/bulletin/ms13-047

## Disclosure Timeline

- 2013-04-16 - Vulnerability reported to vendor
- 2013-06-27 - Coordinated public release of advisory
