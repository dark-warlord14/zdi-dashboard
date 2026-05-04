# ZDI-12-198: Microsoft Internet Explorer CMarkup outerText Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-198
- **ZDI-CAN:** ZDI-CAN-1574
- **Date:** 2012-12-21
- **CVE:** CVE-2012-2557
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer 8
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-198/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the way Internet Explorer handles CMarkup objects. By manipulating a document's elements an attacker can force a dangling pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://technet.microsoft.com/en-us/security/advisory/2757760

## Disclosure Timeline

- 2012-07-24 - Vulnerability reported to vendor
- 2012-12-21 - Coordinated public release of advisory
