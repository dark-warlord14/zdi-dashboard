# ZDI-17-499: Trend Micro Control Manager RestfulServiceUtility.NET SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-499
- **ZDI-CAN:** ZDI-CAN-4638
- **Date:** 2017-07-31
- **CVE:** CVE-2017-11388
- **CVSS:** 6.0
- **CVSS Vector:** AV:N/AC:M/Au:S/C:P/I:P/A:P
- **Affected Vendors:** Trend Micro
- **Affected Products:** Control Manager
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-499/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Trend Micro Control Manager. Authentication is required to exploit this vulnerability. The specific flaw exists within the Investigate endpoint in RestfulServiceUtility.NET.dll. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to execute arbitrary code under the context of NETWORKSERVICE.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/1117722

## Disclosure Timeline

- 2017-03-30 - Vulnerability reported to vendor
- 2017-07-31 - Coordinated public release of advisory
