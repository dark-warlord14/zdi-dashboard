# ZDI-16-407: Eaton ELCSoft ELCSimulator Stack Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-407
- **ZDI-CAN:** ZDI-CAN-3697
- **Date:** 2017-08-07
- **CVE:** CVE-2016-4512
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Eaton
- **Affected Products:** ELCSoft
- **Credit:** Ariele Caltabiano (kimiya)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-407/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Eaton ELCSoft. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of network TCP requests by ELCSimulator.exe. A crafted request will cause a stack buffer overflow. An attacker can leverage this vulnerability to execute arbitrary code in the context of the process.

## Additional Details

Eaton has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-16-182-01

## Disclosure Timeline

- 2016-04-14 - Vulnerability reported to vendor
- 2017-08-07 - Coordinated public release of advisory
