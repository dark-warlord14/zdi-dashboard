# ZDI-14-033: Microsoft Internet Explorer CSelectElement Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-033
- **ZDI-CAN:** ZDI-CAN-2040
- **Date:** 2014-03-20
- **CVE:** CVE-2014-0312
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Simon Zuckerbraun
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-033/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of CSelectElement objects. By manipulating a document's elements an attacker can force a dangling pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/security/bulletin/MS14-012

## Disclosure Timeline

- 2013-11-21 - Vulnerability reported to vendor
- 2014-03-20 - Coordinated public release of advisory
