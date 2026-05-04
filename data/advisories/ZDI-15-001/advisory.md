# ZDI-15-001: Schneider Electric ProClima MetaDraw ObjectOverlappedBy Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-001
- **ZDI-CAN:** ZDI-CAN-2480
- **Date:** 2015-01-07
- **CVE:** CVE-2014-8513
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Schneider Electric
- **Affected Products:** ProClima
- **Credit:** Andrea Micalizzi (rgod)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-001/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Schneider Electric ProClima. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the MetaDraw ActiveX control's ObjectOverlappedBy method. The control dereferences an attacker-supplied memory address and redirects execution flow to the resulting address. An attacker can exploit this condition to achieve code execution under the context of the browser process.

## Additional Details

Schneider Electric has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-14-350-01

## Disclosure Timeline

- 2014-09-03 - Vulnerability reported to vendor
- 2015-01-07 - Coordinated public release of advisory
