# ZDI-22-934: Advantech iView getModulePageContent SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-934
- **ZDI-CAN:** ZDI-CAN-16607
- **Date:** 2022-06-30
- **CVE:** CVE-2022-2142
- **CVSS:** 8.1
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Advantech
- **Affected Products:** iView
- **Credit:** @rgod777
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-934/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Advantech iView. Authentication is not required to exploit this vulnerability. The specific flaw exists within the NetworkServlet endpoint, which listens on TCP port 8080 by default. A crafted request can trigger execution of SQL queries composed from a user-supplied string. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of SYSTEM.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/uscert/ics/advisories/icsa-22-179-03

## Disclosure Timeline

- 2022-03-02 - Vulnerability reported to vendor
- 2022-06-30 - Coordinated public release of advisory
