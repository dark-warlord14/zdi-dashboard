# ZDI-14-405: Microsoft Internet Explorer Insert Command Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-405
- **ZDI-CAN:** ZDI-CAN-2503
- **Date:** 2014-12-09
- **CVE:** CVE-2014-6375
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** sky
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-405/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The vulnerability relates to how Internet Explorer processes HTML elements created using the script method execCommand. An attacker can cause Internet Explorer to allocate memory for such an element and later to reuse the memory after the time it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/ms14-080.aspx

## Disclosure Timeline

- 2014-09-04 - Vulnerability reported to vendor
- 2014-12-09 - Coordinated public release of advisory
