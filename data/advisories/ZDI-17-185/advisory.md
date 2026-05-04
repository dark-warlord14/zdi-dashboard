# ZDI-17-185: Trend Micro Control Manager AdHocQueryExportProcessing SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-185
- **ZDI-CAN:** ZDI-CAN-4116
- **Date:** 2017-09-22
- **CVE:** N/A
- **CVSS:** 6.0
- **CVSS Vector:** AV:N/AC:M/Au:S/C:P/I:P/A:P
- **Affected Vendors:** Trend Micro
- **Affected Products:** Control Manager
- **Credit:** Steven Seeley of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-185/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Trend Micro Control Manager. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within processing of AdHocQueryExportProcessing.aspx. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to execute arbitrary code under the context of NETWORKSERVICE.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/1116863

## Disclosure Timeline

- 2016-11-15 - Vulnerability reported to vendor
- 2017-09-22 - Coordinated public release of advisory
