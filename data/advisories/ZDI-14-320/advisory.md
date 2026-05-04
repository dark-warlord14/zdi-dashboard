# ZDI-14-320: Microsoft Internet Explorer CTableOMRowCache Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-320
- **ZDI-CAN:** ZDI-CAN-2430
- **Date:** 2014-09-16
- **CVE:** CVE-2014-4092
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** A3F2160DCA1BDE70DA1D99ED267D5DC1EC336192
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-320/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The vulnerability relates to how Internet Explorer keeps track of in-memory objects representing rows in an HTML table. By manipulating a document's elements an attacker can force a CTableRow object in memory to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/MS14-052

## Disclosure Timeline

- 2014-07-24 - Vulnerability reported to vendor
- 2014-09-16 - Coordinated public release of advisory
