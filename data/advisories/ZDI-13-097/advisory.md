# ZDI-13-097: Microsoft Internet Explorer CMarkup Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-097
- **ZDI-CAN:** ZDI-CAN-1783
- **Date:** 2013-05-29
- **CVE:** CVE-2013-0090
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** SkyLined
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-097/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists with the handling of DOM manipulations on an embedded child of an <abbr> tag. The process can be made to delete an object resulting in a dangling pointer. The process can be later forced to reuse this pointer resulting in a use-after-free condition. An attacker can leverage this situation to execute code under the context of the user running the browser.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://technet.microsoft.com/en-us/security/bulletin/ms13-021

## Disclosure Timeline

- 2013-02-13 - Vulnerability reported to vendor
- 2013-05-29 - Coordinated public release of advisory
