# ZDI-24-1322: Centreon updateAccessGroupLinks SQL Injection Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1322
- **ZDI-CAN:** ZDI-CAN-24534
- **Date:** 2024-10-08
- **CVE:** CVE-2024-39842
- **CVSS:** 4.7
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Centreon
- **Affected Products:** Centreon
- **Credit:** Simon Humbert of Trend Micro Security Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1322/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on affected installations of Centreon. Authentication is required to exploit this vulnerability. The specific flaw exists within the updateAccessGroupLinks function. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to escalate privileges to resources normally protected from the user.

## Additional Details

Centreon has issued an update to correct this vulnerability. More details can be found at: https://thewatch.centreon.com/latest-security-bulletins-64/security-bulletin-for-centreon-web-3809

## Disclosure Timeline

- 2024-06-21 - Vulnerability reported to vendor
- 2024-10-08 - Coordinated public release of advisory
- 2024-10-08 - Advisory Updated
