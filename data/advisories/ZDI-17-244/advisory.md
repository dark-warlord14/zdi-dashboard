# ZDI-17-244: Trend Micro Control Manager cgiShowClientAdm Missing Authentication for Critical Function Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-244
- **ZDI-CAN:** ZDI-CAN-4511
- **Date:** 2017-04-05
- **CVE:** N/A
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Trend Micro
- **Affected Products:** Control Manager
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-244/
## Vulnerability Details

This vulnerability allows remote attackers to modify the security posture of the underlying product on vulnerable installations of Trend Micro Control Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of calls to the cgiShowClientAdm web function. The software does not provide any authentication for functionality that can expose, modify, and delete DLP templates involved in filtering. An attacker can leverage this vulnerability to modify the security posture of the underlying product.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/1116863

## Disclosure Timeline

- 2017-03-30 - Vulnerability reported to vendor
- 2017-04-05 - Coordinated public release of advisory
