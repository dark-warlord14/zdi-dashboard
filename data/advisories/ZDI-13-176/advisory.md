# ZDI-13-176: Microsoft Internet Explorer column-count Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-176
- **ZDI-CAN:** ZDI-CAN-1841
- **Date:** 2013-07-26
- **CVE:** CVE-2013-3146
- **CVSS:** 5.1
- **CVSS Vector:** AV:N/AC:H/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Toan Pham Van aka @__suto
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-176/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the column-count CSS property. The issue lies in the failure to properly validate input before using it to allocate a buffer on the heap. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/security/bulletin/ms13-055

## Disclosure Timeline

- 2013-04-16 - Vulnerability reported to vendor
- 2013-07-26 - Coordinated public release of advisory
