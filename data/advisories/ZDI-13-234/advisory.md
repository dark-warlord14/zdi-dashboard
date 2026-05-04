# ZDI-13-234: Microsoft Internet Explorer CFontElement Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-234
- **ZDI-CAN:** ZDI-CAN-1942
- **Date:** 2013-10-08
- **CVE:** CVE-2013-3874
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** AMol NAik & a garage4hackers member
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-234/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of CFontElement objects. By manipulating a document's elements an attacker can force a dangling pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/security/bulletin/ms13-080

## Disclosure Timeline

- 2013-07-23 - Vulnerability reported to vendor
- 2013-10-08 - Coordinated public release of advisory
