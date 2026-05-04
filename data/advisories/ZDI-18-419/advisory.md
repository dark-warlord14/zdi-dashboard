# ZDI-18-419: Trend Micro Encryption for Email Gateway formChangePass username SQL Injection Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-419
- **ZDI-CAN:** ZDI-CAN-5594
- **Date:** 2018-05-04
- **CVE:** CVE-2018-10353
- **CVSS:** 3.5
- **CVSS Vector:** AV:N/AC:M/Au:S/C:P/I:N/A:N
- **Affected Vendors:** Trend Micro
- **Affected Products:** Encryption for Email Gateway
- **Credit:** Steven Seeley of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-419/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Trend Micro Encryption for Email Gateway. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the formChangePass class. When parsing the username parameter, the process does not properly validate a user-supplied string before using it to construct SQL queries. An attacker can leverage this in conjunction with other vulnerabilities to disclose sensitive information under the context of the database.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/1119349

## Disclosure Timeline

- 2018-01-19 - Vulnerability reported to vendor
- 2018-05-04 - Coordinated public release of advisory
- 2018-05-04 - Advisory Updated
