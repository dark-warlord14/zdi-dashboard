# ZDI-16-230: Microsoft Internet Explorer CMediaEngine Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-230
- **ZDI-CAN:** ZDI-CAN-3404
- **Date:** 2016-04-12
- **CVE:** CVE-2016-0166
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Henry Li(zenhumany) of Trend Micro
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-230/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of CMediaEngine objects. By manipulating a document's elements an attacker can force a dangling pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS16-037

## Disclosure Timeline

- 2015-11-09 - Vulnerability reported to vendor
- 2016-04-12 - Coordinated public release of advisory
