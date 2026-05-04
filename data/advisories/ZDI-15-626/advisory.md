# ZDI-15-626: Schneider Electric ProClima F1BookView ActiveX Control CopyAll Method Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-626
- **ZDI-CAN:** ZDI-CAN-3056
- **Date:** 2015-12-08
- **CVE:** CVE-2015-8561
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Schneider Electric
- **Affected Products:** ProClima
- **Credit:** Ariele Caltabiano
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-626/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Schneider Electric ProClima. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the implementation of the CopyAll method of the F1BookView ActiveX control. The method accepts an integer value and interprets it as the address of a structure in memory. An attacker can leverage this vulnerability to achieve code execution under the context of the process.

## Additional Details

Schneider Electric has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-15-335-02

## Disclosure Timeline

- 2015-07-28 - Vulnerability reported to vendor
- 2015-12-08 - Coordinated public release of advisory
