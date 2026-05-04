# ZDI-17-131: Trend Micro SafeSync for Enterprise count_ad_members SQL Injection Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-131
- **ZDI-CAN:** ZDI-CAN-4409
- **Date:** 2017-03-01
- **CVE:** N/A
- **CVSS:** 4.0
- **CVSS Vector:** AV:N/AC:L/Au:S/C:P/I:N/A:N
- **Affected Vendors:** Trend Micro
- **Affected Products:** SafeSync for Enterprise
- **Credit:** Roberto Suggi Liverani - @malerisch - http://blog.malerisch.net/ & Steven Seeley of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-131/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Trend Micro SafeSync for Enterprise. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the count_ad_members function. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to disclose information under the context of the database.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/1116749

## Disclosure Timeline

- 2017-02-02 - Vulnerability reported to vendor
- 2017-03-01 - Coordinated public release of advisory
