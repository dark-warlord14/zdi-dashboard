# ZDI-22-953: Centreon Poller Resource SQL Injection Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-953
- **ZDI-CAN:** ZDI-CAN-16335
- **Date:** 2022-07-07
- **CVE:** CVE-2022-34871
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Centreon
- **Affected Products:** Centreon
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-953/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on affected installations of Centreon. Authentication is required to exploit this vulnerability. The specific flaw exists within the configuration of poller resources. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to escalate privileges to the level of an administrator.

## Additional Details

Centreon has issued an update to correct this vulnerability. More details can be found at: https://docs.centreon.com/docs/21.10/releases/centreon-core/

## Disclosure Timeline

- 2022-02-16 - Vulnerability reported to vendor
- 2022-07-07 - Coordinated public release of advisory
- 2022-08-03 - Advisory Updated
