# ZDI-14-399: PTC IsoView ActiveX Control ViewPort Heap Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-399
- **ZDI-CAN:** ZDI-CAN-2190
- **Date:** 2014-12-04
- **CVE:** CVE-2014-9267
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** PTC
- **Affected Products:** IsoView ActiveX Control
- **Credit:** Andrea Micalizzi (rgod)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-399/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of the PTC IsoView ActiveX control. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the ViewPort property of the control. By setting the property to a malicious value, an attacker can overflow a statically allocated heap buffer. This could allow the attacker to execute arbitrary code in the context of the browser.

## Additional Details

PTC has issued an update to correct this vulnerability. More details can be found at: https://support.ptc.com/appserver/cs/view/solution.jsp?n=CS181001

## Disclosure Timeline

- 2014-05-20 - Vulnerability reported to vendor
- 2014-12-04 - Coordinated public release of advisory
