# ZDI-15-548: AlienVault Unified Security Management Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-548
- **ZDI-CAN:** ZDI-CAN-3020
- **Date:** 2015-11-10
- **CVE:** N/A
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** AlienVault
- **Affected Products:** Unified Security Management
- **Credit:** agix
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-548/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges to root on vulnerable installations of AlienVault Unified Security Management. Authentication is not required to exploit this vulnerability. The specific flaw exists within the configuration of the server and database. A local attacker in the alienvault group can read the database password and schedule, as root, a custom report that can include shell commands. This vulnerability can be leveraged by a local attacker to execute arbitrary code as root.

## Additional Details

AlienVault has issued an update to correct this vulnerability. More details can be found at: https://www.alienvault.com/forums/discussion/5127/

## Disclosure Timeline

- 2015-06-25 - Vulnerability reported to vendor
- 2015-11-10 - Coordinated public release of advisory
