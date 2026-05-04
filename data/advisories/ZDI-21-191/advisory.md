# ZDI-21-191: Advantech iView UserServlet SQL Injection Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-191
- **ZDI-CAN:** ZDI-CAN-12344
- **Date:** 2021-02-11
- **CVE:** CVE-2021-22658
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Advantech
- **Affected Products:** iView
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-191/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on affected installations of Advantech iView. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the UserServlet class. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to escalate privileges and reset the password for the Admin user.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://us-cert.cisa.gov/ics/advisories/icsa-21-040-02

## Disclosure Timeline

- 2020-12-02 - Vulnerability reported to vendor
- 2021-02-11 - Coordinated public release of advisory
