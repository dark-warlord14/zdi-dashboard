# ZDI-13-083: Microsoft Internet Explorer CDispNode Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-083
- **ZDI-CAN:** ZDI-CAN-1694
- **Date:** 2013-05-29
- **CVE:** CVE-2013-1309
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** SkyLined
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-083/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within styles being applied to elements on the DOM causing a negatively positioned CDispNode to be freed. The process can be later forced to reuse this object resulting in a use-after-free condition. An attacker can leverage this situation to execute code under the context of the user running the browser.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/security/bulletin/ms13-037

## Disclosure Timeline

- 2013-02-04 - Vulnerability reported to vendor
- 2013-05-29 - Coordinated public release of advisory
