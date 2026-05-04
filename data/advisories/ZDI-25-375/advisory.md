# ZDI-25-375: Trend Micro Endpoint Encryption ProcessWhereClause SQL Injection Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-375
- **ZDI-CAN:** ZDI-CAN-25526
- **Date:** 2025-06-11
- **CVE:** CVE-2025-49218
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Endpoint Encryption
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-375/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on affected installations of Trend Micro Endpoint Encryption. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the implementation of the ProcessWhereClause method. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to escalate privileges to resources normally protected from the user.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/en-US/solution/KA-0019928

## Disclosure Timeline

- 2024-10-11 - Vulnerability reported to vendor
- 2025-06-11 - Coordinated public release of advisory
- 2025-06-11 - Advisory Updated
