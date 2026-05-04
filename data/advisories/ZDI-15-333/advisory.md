# ZDI-15-333: Microsoft Internet Explorer CTableRow Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-333
- **ZDI-CAN:** ZDI-CAN-2873
- **Date:** 2015-07-14
- **CVE:** CVE-2015-2406
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** B6BEB4D5E828CF0CCB47BB24AAC22515
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-333/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of CTableRow objects. By manipulating a document's elements, an attacker can force a dangling pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/MS15-065

## Disclosure Timeline

- 2015-04-09 - Vulnerability reported to vendor
- 2015-07-14 - Coordinated public release of advisory
