# ZDI-13-164: Microsoft Internet Explorer CElement Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-164
- **ZDI-CAN:** ZDI-CAN-1848
- **Date:** 2013-07-26
- **CVE:** CVE-2013-3150
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Omair
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-164/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within reusing a CElement object after it has been freed. This object can be used after freed by the setCapture event method. An attacker can leverage this situation to execute code under the context of the user running the browser.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/security/bulletin/ms13-055

## Disclosure Timeline

- 2013-04-16 - Vulnerability reported to vendor
- 2013-07-26 - Coordinated public release of advisory
