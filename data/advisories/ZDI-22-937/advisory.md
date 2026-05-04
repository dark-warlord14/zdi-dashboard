# ZDI-22-937: Advantech iView set_useraccount UserName SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-937
- **ZDI-CAN:** ZDI-CAN-16773
- **Date:** 2022-06-30
- **CVE:** CVE-2022-2136
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Advantech
- **Affected Products:** iView
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-937/
## Vulnerability Details

This vulnerability allows remote attackers to create arbitrary files on affected installations of Advantech iView. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the NetworkServlet endpoint, which listens on TCP port 8080 by default. When parsing the UserName element of the set_useraccount action, the process does not properly validate a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/uscert/ics/advisories/icsa-22-179-03

## Disclosure Timeline

- 2022-03-23 - Vulnerability reported to vendor
- 2022-06-30 - Coordinated public release of advisory
- 2022-07-14 - Advisory Updated
