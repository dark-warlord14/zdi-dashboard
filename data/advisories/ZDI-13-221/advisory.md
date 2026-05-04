# ZDI-13-221: Microsoft Internet Explorer CSegment Object Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-221
- **ZDI-CAN:** ZDI-CAN-1913
- **Date:** 2013-09-11
- **CVE:** CVE-2013-3209
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-221/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the usage of execCommand("selectAll") and selection.clear which can cause a CSegment object to be freed. The process can be later forced to reuse this pointer resulting in a use-after-free condition. An attacker can leverage this situation to execute code under the context of the user running the browser.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/security/bulletin/ms13-069

## Disclosure Timeline

- 2013-06-21 - Vulnerability reported to vendor
- 2013-09-11 - Coordinated public release of advisory
