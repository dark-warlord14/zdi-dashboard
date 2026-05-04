# ZDI-13-084: Microsoft Internet Explorer CMarkup Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-084
- **ZDI-CAN:** ZDI-CAN-1788
- **Date:** 2013-05-29
- **CVE:** CVE-2013-3140
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** e6af8de8b1d4b2b6d5ba2610cbf9cd38
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-084/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of CMarkup objects. By manipulating a document's elements an attacker can force a dangling pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/security/bulletin/ms13-037

## Disclosure Timeline

- 2013-02-22 - Vulnerability reported to vendor
- 2013-05-29 - Coordinated public release of advisory
