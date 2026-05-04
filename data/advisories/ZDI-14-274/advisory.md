# ZDI-14-274: Microsoft Internet Explorer CSegment Object Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-274
- **ZDI-CAN:** ZDI-CAN-2184
- **Date:** 2014-08-12
- **CVE:** CVE-2014-4063
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-274/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the usage of execCommand("selectAll") and styles which can cause a CSegment object to be freed. The process can be later forced to reuse this pointer resulting in a use-after-free condition. An attacker can leverage this situation to execute code under the context of the user running the browser.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/MS14-051

## Disclosure Timeline

- 2014-03-07 - Vulnerability reported to vendor
- 2014-08-12 - Coordinated public release of advisory
