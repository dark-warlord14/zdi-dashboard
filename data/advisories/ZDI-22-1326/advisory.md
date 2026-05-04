# ZDI-22-1326: Centreon Poller Resource SQL Injection Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1326
- **ZDI-CAN:** ZDI-CAN-18304
- **Date:** 2022-10-03
- **CVE:** CVE-2022-41142
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Centreon
- **Affected Products:** Centreon
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1326/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on affected installations of Centreon. Authentication is required to exploit this vulnerability. The specific flaw exists within the handling of requests to configure poller resources. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to escalate privileges to the level of an administrator.

## Additional Details

Centreon has issued an update to correct this vulnerability. More details can be found at: https://github.com/centreon/centreon/security/policy

## Disclosure Timeline

- 2022-08-23 - Vulnerability reported to vendor
- 2022-10-03 - Coordinated public release of advisory
