# ZDI-17-496: Trend Micro Control Manager cmdHandlerNewReportScheduler SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-496
- **ZDI-CAN:** ZDI-CAN-4549
- **Date:** 2017-08-02
- **CVE:** CVE-2017-11386
- **CVSS:** 7.8
- **CVSS Vector:** AV:N/AC:L/Au:N/C:N/I:C/A:N
- **Affected Vendors:** Trend Micro
- **Affected Products:** Control Manager
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-496/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on vulnerable installations of Trend Micro Control Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within cmdHandlerNewReportScheduler.dll when executing opcode 0x4707. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the database.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/1117722

## Disclosure Timeline

- 2017-03-23 - Vulnerability reported to vendor
- 2017-08-02 - Coordinated public release of advisory
