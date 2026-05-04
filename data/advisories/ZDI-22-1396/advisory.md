# ZDI-22-1396: Centreon Poller Broker SQL Injection Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1396
- **ZDI-CAN:** ZDI-CAN-18555
- **Date:** 2022-10-07
- **CVE:** CVE-2022-42425
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Centreon
- **Affected Products:** Centreon
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1396/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on affected installations of Centreon. Authentication is required to exploit this vulnerability. The specific flaw exists within the handling of requests to modify poller broker configuration. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to escalate privileges to the level of an administrator.

## Additional Details

Fixed in centreon-web-21.04.19, centreon-web-21.10.11 and centreon-web-22.04.6 https://github.com/centreon/centreon/security/policy

## Disclosure Timeline

- 2022-09-06 - Vulnerability reported to vendor
- 2022-10-07 - Coordinated public release of advisory
