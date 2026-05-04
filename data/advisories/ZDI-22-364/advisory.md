# ZDI-22-364: MariaDB CONNECT Storage Engine Use-After-Free Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-364
- **ZDI-CAN:** ZDI-CAN-16207
- **Date:** 2022-02-16
- **CVE:** CVE-2022-24050
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** MariaDB
- **Affected Products:** MariaDB
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-364/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of MariaDB. Authentication is required to exploit this vulnerability. The specific flaw exists within the processing of SQL queries. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the service account.

## Additional Details

MariaDB has issued an update to correct this vulnerability. More details can be found at: https://mariadb.com/kb/en/security/

## Disclosure Timeline

- 2022-01-20 - Vulnerability reported to vendor
- 2022-02-16 - Coordinated public release of advisory
