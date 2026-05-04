# ZDI-13-198: Microsoft Internet Explorer CMarkup Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-198
- **ZDI-CAN:** ZDI-CAN-1867
- **Date:** 2013-08-13
- **CVE:** CVE-2013-3194
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Arthur Gerkis
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-198/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within CMarkup::DisconnectTreePos where destruction of a rendered attacker page by close of a tab or browser will trigger a use-after-free vulnerability in this function. An attacker can leverage this vulnerability to execute code under the context of the process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/security/bulletin/ms13-059

## Disclosure Timeline

- 2013-05-13 - Vulnerability reported to vendor
- 2013-08-13 - Coordinated public release of advisory
