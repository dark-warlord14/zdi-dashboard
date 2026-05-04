# ZDI-13-025: Microsoft Internet Explorer COmWindowProxy Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-025
- **ZDI-CAN:** ZDI-CAN-1598
- **Date:** 2013-02-14
- **CVE:** CVE-2013-0019
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** SkyLined
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-025/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of iframes. By manipulating an iframe using window.open an attacker can force a dangling pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://technet.microsoft.com/en-us/security/bulletin/MS13-009

## Disclosure Timeline

- 2012-11-09 - Vulnerability reported to vendor
- 2013-02-14 - Coordinated public release of advisory
