# ZDI-22-928: Advantech iView NetworkServlet clearDatabase Missing Authentication Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-928
- **ZDI-CAN:** ZDI-CAN-16688
- **Date:** 2022-06-30
- **CVE:** CVE-2022-2138
- **CVSS:** 8.2
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:H
- **Affected Vendors:** Advantech
- **Affected Products:** iView
- **Credit:** @rgod777
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-928/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Advantech iView. Authentication is not required to exploit this vulnerability. The specific flaw exists within the NetworkServlet endpoint, which listens on TCP port 8080 by default. The issue results from the lack of authentication prior to allowing access to the clearDatabase functionality. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/uscert/ics/advisories/icsa-22-179-03

## Disclosure Timeline

- 2022-03-04 - Vulnerability reported to vendor
- 2022-06-30 - Coordinated public release of advisory
