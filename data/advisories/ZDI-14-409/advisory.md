# ZDI-14-409: Microsoft Internet Explorer CInputElement Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-409
- **ZDI-CAN:** ZDI-CAN-2536
- **Date:** 2014-12-09
- **CVE:** CVE-2014-8966
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** sky
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-409/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of of CInput elements. By manipulating a document's elements an attacker can force a type confusion error while processing an element's event handler. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/ms14-080.aspx

## Disclosure Timeline

- 2014-09-29 - Vulnerability reported to vendor
- 2014-12-09 - Coordinated public release of advisory
