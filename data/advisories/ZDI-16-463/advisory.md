# ZDI-16-463: Moxa SoftCMS getcaminfo SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-463
- **ZDI-CAN:** ZDI-CAN-3757
- **Date:** 2016-08-10
- **CVE:** CVE-2016-5792
- **CVSS:** 9.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Moxa
- **Affected Products:** SoftCMS
- **Credit:** Zhou Yu
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-463/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Moxa SoftCMS. Authentication is not required to exploit this vulnerability. The specific flaw exists within the getcaminfo.asp script. When parsing the VWID element, the process fails to properly validate a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to execute arbitrary code in the context of the database access process, which runs as Administrator.

## Additional Details

Moxa has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-16-215-01

## Disclosure Timeline

- 2016-06-23 - Vulnerability reported to vendor
- 2016-08-10 - Coordinated public release of advisory
