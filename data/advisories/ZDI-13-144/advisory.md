# ZDI-13-144: Microsoft Internet Explorer CCaret Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-144
- **ZDI-CAN:** ZDI-CAN-1819
- **Date:** 2013-06-27
- **CVE:** CVE-2013-3123
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Aniway.Anyway@gmail.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-144/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the CCaret object. When triggering the onscroll event, the process can be made to delete a CCaret object resulting in a dangling pointer. The process can be later forced to reuse this pointer resulting in a use-after-free condition. An attacker can leverage this situation to execute code under the context of the user running the browser.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://technet.microsoft.com/en-us/security/bulletin/ms13-047

## Disclosure Timeline

- 2013-03-29 - Vulnerability reported to vendor
- 2013-06-27 - Coordinated public release of advisory
