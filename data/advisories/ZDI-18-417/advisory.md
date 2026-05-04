# ZDI-18-417: Trend Micro Encryption for Email Gateway emailSearch SearchString SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-417
- **ZDI-CAN:** ZDI-CAN-5553
- **Date:** 2018-05-04
- **CVE:** CVE-2018-6230
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/Au:S/C:P/I:P/A:P
- **Affected Vendors:** Trend Micro
- **Affected Products:** Encryption for Email Gateway
- **Credit:** Steven Seeley (mr_me) of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-417/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary SQL statements on vulnerable installations of Trend Micro Encryption for Email Gateway. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the wsEmailSearch class. When parsing the SearchString parameter, the process does not properly validate a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to execute code under the context of root.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/1119349

## Disclosure Timeline

- 2018-01-02 - Vulnerability reported to vendor
- 2018-05-04 - Coordinated public release of advisory
- 2018-05-04 - Advisory Updated
