# ZDI-14-355: Microsoft Internet Explorer CTableCell Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-355
- **ZDI-CAN:** ZDI-CAN-2398
- **Date:** 2014-10-14
- **CVE:** CVE-2014-4092
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** A3F2160DCA1BDE70DA1D99ED267D5DC1EC336192
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-355/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of CTableCell objects. By manipulating a document's elements an attacker can force a dangling pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS14-052

## Disclosure Timeline

- 2014-07-07 - Vulnerability reported to vendor
- 2014-10-14 - Coordinated public release of advisory
