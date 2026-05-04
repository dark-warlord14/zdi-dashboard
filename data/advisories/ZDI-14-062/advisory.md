# ZDI-14-062: Microsoft Internet Explorer NavigateToBookmark Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-062
- **ZDI-CAN:** ZDI-CAN-2100
- **Date:** 2014-04-08
- **CVE:** CVE-2014-0285
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Simon Zuckerbraun
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-062/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the function NavigateToBookmark. By manipulating a document's elements an attacker can force a dangling pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://go.microsoft.com/fwlink/?LinkID=390977

## Disclosure Timeline

- 2014-02-18 - Vulnerability reported to vendor
- 2014-04-08 - Coordinated public release of advisory
