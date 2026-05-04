# ZDI-13-224: Microsoft Internet Explorer CHtmParse Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-224
- **ZDI-CAN:** ZDI-CAN-1863
- **Date:** 2013-09-11
- **CVE:** CVE-2013-3201
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer 9
- **Credit:** Jose A. Vazquez of Yenteasy - Security Research -
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-224/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of DOM manipulation. Using this vulnerability, an attacker is able to cause a use-after-free condition. This allows for an attacker to execute arbitrary code in the context of the browser.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/security/bulletin/ms13-069

## Disclosure Timeline

- 2013-05-13 - Vulnerability reported to vendor
- 2013-09-11 - Coordinated public release of advisory
