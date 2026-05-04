# ZDI-17-497: Trend Micro Control Manager Debug Level Authentication Bypass Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-497
- **ZDI-CAN:** ZDI-CAN-4512
- **Date:** 2017-07-31
- **CVE:** CVE-2017-11387
- **CVSS:** 5.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Trend Micro
- **Affected Products:** Control Manager
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-497/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Trend Micro Control Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of debug settings. The software does not provide authentication validation for functionality that can change debug logging levels and provides incorrect authentication validation for exposing debug information. An attacker can leverage this vulnerability to expose sensitive information.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/1117722

## Disclosure Timeline

- 2017-03-30 - Vulnerability reported to vendor
- 2017-07-31 - Coordinated public release of advisory
