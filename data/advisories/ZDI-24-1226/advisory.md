# ZDI-24-1226: mySCADA myPRO Hard-Coded Credentials Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1226
- **ZDI-CAN:** ZDI-CAN-23546
- **Date:** 2024-09-13
- **CVE:** CVE-2024-4708
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** mySCADA
- **Affected Products:** myPRO
- **Credit:** Nassim Asrir
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1226/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of mySCADA myPRO. Authentication is not required to exploit this vulnerability. The specific flaw exists within the telnet service, which listens on TCP port 5005 by default. The issue results from the use of hard-coded credentials. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

mySCADA has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-24-184-02

## Disclosure Timeline

- 2024-03-27 - Vulnerability reported to vendor
- 2024-09-13 - Coordinated public release of advisory
- 2024-09-13 - Advisory Updated
