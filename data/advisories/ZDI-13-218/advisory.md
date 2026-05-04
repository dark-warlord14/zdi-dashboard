# ZDI-13-218: Microsoft Internet Explorer CWindow Destructor Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-218
- **ZDI-CAN:** ZDI-CAN-1893
- **Date:** 2013-09-11
- **CVE:** CVE-2013-3206
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Arthur Gerkis
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-218/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the unloading of pages. By manipulating the load and unload process, an attacker is able to create a use-after-free condition. With this, an attacker is able to execute arbitrary code in the context of the browser.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/security/bulletin/ms13-069

## Disclosure Timeline

- 2013-06-10 - Vulnerability reported to vendor
- 2013-09-11 - Coordinated public release of advisory
