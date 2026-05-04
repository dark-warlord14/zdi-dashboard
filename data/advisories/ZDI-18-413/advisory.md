# ZDI-18-413: Trend Micro Encryption for Email Gateway editPolicy editRuleId SQL Injection Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-413
- **ZDI-CAN:** ZDI-CAN-5533
- **Date:** 2018-05-04
- **CVE:** CVE-2018-6229
- **CVSS:** 4.0
- **CVSS Vector:** AV:N/AC:L/Au:S/C:P/I:N/A:N
- **Affected Vendors:** Trend Micro
- **Affected Products:** Encryption for Email Gateway
- **Credit:** Steven Seeley (mr_me) of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-413/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Trend Micro Encryption for Email Gateway. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the formEditPolicy class. When parsing the editRuleId parameter, the process does not properly validate a user-supplied string before using it to construct SQL queries. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of root.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/1119349

## Disclosure Timeline

- 2018-01-02 - Vulnerability reported to vendor
- 2018-05-04 - Coordinated public release of advisory
- 2018-05-04 - Advisory Updated
