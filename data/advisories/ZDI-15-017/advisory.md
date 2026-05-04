# ZDI-15-017: Microsoft Internet Explorer CIFrameElement Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-017
- **ZDI-CAN:** ZDI-CAN-2608
- **Date:** 2015-02-10
- **CVE:** CVE-2015-0035
- **CVSS:** 5.1
- **CVSS Vector:** AV:N/AC:H/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** sky
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-017/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The vulnerability relates to how Internet Explorer displays iframe elements. By manipulating a document's elements an attacker can force a CIFrameElement object in memory to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS15-009

## Disclosure Timeline

- 2014-11-04 - Vulnerability reported to vendor
- 2015-02-10 - Coordinated public release of advisory
