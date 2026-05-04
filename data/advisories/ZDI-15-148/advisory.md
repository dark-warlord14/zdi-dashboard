# ZDI-15-148: Novell Zenworks schedule.ScheduleQuery SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-148
- **ZDI-CAN:** ZDI-CAN-2576
- **Date:** 2015-04-22
- **CVE:** CVE-2015-0782
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Novell
- **Affected Products:** Zenworks
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-148/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell Zenworks. Authentication is not required to exploit this vulnerability. The specific flaw exists within the ScheduleQuery method of the schedule class. The issue lies in the failure to sanitize user-supplied input prior to executing a SQL statement. An attacker could leverage this vulnerability to execute code under the context of the database.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: https://www.novell.com/support/kb/doc.php?id=7016431

## Disclosure Timeline

- 2015-01-15 - Vulnerability reported to vendor
- 2015-04-22 - Coordinated public release of advisory
