# ZDI-14-285: Microsoft Internet Explorer first-letter Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-285
- **ZDI-CAN:** ZDI-CAN-2309
- **Date:** 2014-08-12
- **CVE:** CVE-2014-4050
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Omair
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-285/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the styling of first-letter elements. By manipulating a document's elements and styles an attacker can force a dangling pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/MS14-051

## Disclosure Timeline

- 2014-05-08 - Vulnerability reported to vendor
- 2014-08-12 - Coordinated public release of advisory
