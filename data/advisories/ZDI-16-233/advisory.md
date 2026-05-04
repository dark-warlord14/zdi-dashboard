# ZDI-16-233: Microsoft Edge Proxy Object Universal Cross Site Scripting Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-233
- **ZDI-CAN:** ZDI-CAN-3529
- **Date:** 2016-04-12
- **CVE:** CVE-2016-0158
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Edge
- **Credit:** lokihardt
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-233/
## Vulnerability Details

This vulnerability allows remote attackers to inject arbitrary script code into arbitrary domains on vulnerable installations of Microsoft Edge. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the implementation of the JavaScript Proxy object. By performing certain script actions, an attacker can use the Proxy object to inject arbitrary JavaScript code into arbitrary domains, also known as Universal Cross Site Scripting (UXSS). An attacker can leverage this to perform actions on web sites to which the user has access, as well as disclose information from those sites.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS16-038

## Disclosure Timeline

- 2016-01-26 - Vulnerability reported to vendor
- 2016-04-12 - Coordinated public release of advisory
