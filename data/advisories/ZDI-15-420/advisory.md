# ZDI-15-420: Microsoft Internet Explorer Embedded Windows Media Player Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-420
- **ZDI-CAN:** ZDI-CAN-2991
- **Date:** 2015-09-08
- **CVE:** CVE-2015-2487
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Pawel Wylecial
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-420/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The vulnerability relates to how Internet Explorer interacts with Windows Media Player when the latter is used to perform media as part of a web page. By manipulating a document's elements an attacker can cause an object in memory to be reused after it has been freed. Depending on the attack, the object may be of type CMarkup (defined in MSHTML.dll) or of type CWMPPropUpdate (defined in wmp.dll). An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/ms15-094

## Disclosure Timeline

- 2015-06-01 - Vulnerability reported to vendor
- 2015-09-08 - Coordinated public release of advisory
