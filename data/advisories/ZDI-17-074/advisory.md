# ZDI-17-074: Trend Micro Control Manager ProgressReportCGI SQL Injection Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-074
- **ZDI-CAN:** ZDI-CAN-4113
- **Date:** 2017-09-22
- **CVE:** N/A
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Trend Micro
- **Affected Products:** Control Manager
- **Credit:** Steven Seeley of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-074/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Trend Micro Control Manager. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within processing of ProgressReportCGI.exe. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to discover the name and the hashed password of the administrative user.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/1116624

## Disclosure Timeline

- 2016-11-23 - Vulnerability reported to vendor
- 2017-09-22 - Coordinated public release of advisory
