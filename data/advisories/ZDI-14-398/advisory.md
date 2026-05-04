# ZDI-14-398: PTC IsoView Activex Control Multiple Animation Methods Stack Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-398
- **ZDI-CAN:** ZDI-CAN-2189
- **Date:** 2014-12-04
- **CVE:** CVE-2014-9267
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** PTC
- **Affected Products:** IsoView ActiveX Control
- **Credit:** Andrea Micalizzi (rgod)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-398/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of the PTC IsoView ActiveX control. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the arguments to a set of animation related methods. By providing an overly long Object identifier, an attacker can cause a stack buffer overflow. This overflow would allow an attacker to execute arbitrary code in the context of the browser.

## Additional Details

https://support.ptc.com/appserver/cs/view/solution.jsp?n=CS181001

## Disclosure Timeline

- 2014-05-20 - Vulnerability reported to vendor
- 2014-12-04 - Coordinated public release of advisory
