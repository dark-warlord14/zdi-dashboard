# ZDI-22-897: Advantech iView getChassisList SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-897
- **ZDI-CAN:** ZDI-CAN-16695
- **Date:** 2022-06-30
- **CVE:** CVE-2022-2135
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Advantech
- **Affected Products:** iView
- **Credit:** @rgod777
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-897/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Advantech iView. Authentication is not required to exploit this vulnerability. The specific flaw exists within the NetworkServlet endpoint, which listens on TCP port 8080 by default. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/uscert/ics/advisories/icsa-22-179-03

## Disclosure Timeline

- 2022-03-09 - Vulnerability reported to vendor
- 2022-06-30 - Coordinated public release of advisory
