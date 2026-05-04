# ZDI-18-077: Trend Micro Control Manager ViolationCntByChannel SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-077
- **ZDI-CAN:** ZDI-CAN-5182
- **Date:** 2018-01-10
- **CVE:** CVE-2018-3605
- **CVSS:** 6.0
- **CVSS Vector:** AV:N/AC:M/Au:S/C:P/I:P/A:P
- **Affected Vendors:** Trend Micro
- **Affected Products:** Control Manager
- **Credit:** Steven Seeley (mr_me) of Offensive Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-077/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Trend Micro Control Manager. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the ViolationCntByChannel method, which is called by the reporting servlet. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to execute code under the context of the Network Service account.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/1119158

## Disclosure Timeline

- 2017-09-05 - Vulnerability reported to vendor
- 2018-01-10 - Coordinated public release of advisory
