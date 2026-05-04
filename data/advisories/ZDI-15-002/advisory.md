# ZDI-15-002: Schneider Electric ProClima MetaDraw ObjLinks Property Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-002
- **ZDI-CAN:** ZDI-CAN-2483
- **Date:** 2015-01-07
- **CVE:** CVE-2014-8514
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Schneider Electric
- **Affected Products:** ProClima
- **Credit:** Ariele Caltabiano (kimiya)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-002/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Schneider Electric ProClima. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the MetaDraw ActiveX control's ObjLinks property. This property can be assigned an attacker-supplied memory address and the control will redirect execution flow to this given memory address. An attacker can exploit this condition to achieve code execution under the context of the browser process.

## Additional Details

Schneider Electric has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-14-350-01

## Disclosure Timeline

- 2014-09-03 - Vulnerability reported to vendor
- 2015-01-07 - Coordinated public release of advisory
