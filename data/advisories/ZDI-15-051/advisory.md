# ZDI-15-051: PTC Creo View Heap Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-051
- **ZDI-CAN:** ZDI-CAN-2198
- **Date:** 2015-02-27
- **CVE:** CVE-2015-2061
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** PTC
- **Affected Products:** Creo View
- **Credit:** Andrea Micalizzi (rgod)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-051/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of PTC Creo View. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the Creo View browser plugin. An attacker can trigger a heap overflow, by setting a large buffer to a specific attribute. This would allow an attacker to execute arbitrary code in the context of the browser.

## Additional Details

PTC has issued an update to correct this vulnerability. More details can be found at: https://support.ptc.com/appserver/cs/view/solution.jsp?n=CS172389

## Disclosure Timeline

- 2014-05-20 - Vulnerability reported to vendor
- 2015-02-27 - Coordinated public release of advisory
