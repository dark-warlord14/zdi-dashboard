# ZDI-20-1431: FreeBSD FTPD Improper Handling of Exceptional Conditions Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1431
- **ZDI-CAN:** ZDI-CAN-11632
- **Date:** 2020-12-15
- **CVE:** CVE-2020-7468
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** FreeBSD
- **Affected Products:** FTPD
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1431/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on affected installations of FreeBSD FTPD. Authentication is required to exploit this vulnerability. The specific flaw exists within the enforcement of permissions. The process does not properly handle exceptional conditions. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of root.

## Additional Details

FreeBSD has issued an update to correct this vulnerability. More details can be found at: https://security.FreeBSD.org/advisories/FreeBSD-SA-20:30.ftpd.asc

## Disclosure Timeline

- 2020-08-21 - Vulnerability reported to vendor
- 2020-12-15 - Coordinated public release of advisory
