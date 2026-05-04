# ZDI-15-627: Schneider Electric ProClima F1BookView ActiveX Control CopyRange/SwapTables Methods Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-627
- **ZDI-CAN:** ZDI-CAN-3055
- **Date:** 2015-12-08
- **CVE:** CVE-2015-8561
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Schneider Electric
- **Affected Products:** ProClima
- **Credit:** Ariele Caltabiano (Kimiya)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-627/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Schneider Electric ProClima. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaws exist within the implementation of the CopyRange and SwapTable methods of the F1BookView ActiveX control. The methods accept integer values and interpret them as addresses of structures in memory. An attacker can leverage this vulnerability to achieve code execution in the context of the process.

## Additional Details

Schneider Electric has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-15-335-02

## Disclosure Timeline

- 2015-07-28 - Vulnerability reported to vendor
- 2015-12-08 - Coordinated public release of advisory
