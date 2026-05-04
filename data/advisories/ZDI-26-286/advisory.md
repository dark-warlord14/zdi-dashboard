# ZDI-26-286: DriveLock SQL Injection Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-286
- **ZDI-CAN:** ZDI-CAN-28726
- **Date:** 2026-04-15
- **CVE:** CVE-2026-5490
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** DriveLock
- **Affected Products:** DriveLock
- **Credit:** stuxxn
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-286/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on affected installations of DriveLock. Authentication is required to exploit this vulnerability. The specific flaw exists within the web service, which listens on TCP port 4568 by default. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to escalate privileges to resources normally protected from the user.

## Additional Details

DriveLock has issued an update to correct this vulnerability. More details can be found at: https://drivelock.help/sb/Content/SecurityBulletins/26-002-SQLInjection.htm

## Disclosure Timeline

- 2026-02-06 - Vulnerability reported to vendor
- 2026-04-15 - Coordinated public release of advisory
- 2026-04-15 - Advisory Updated
