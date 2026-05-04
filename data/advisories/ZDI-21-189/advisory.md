# ZDI-21-189: Advantech iView CommandServlet Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-189
- **ZDI-CAN:** ZDI-CAN-12096
- **Date:** 2021-02-11
- **CVE:** CVE-2021-22656
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Advantech
- **Affected Products:** iView
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-189/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Advantech iView. Authentication is not required to exploit this vulnerability. The specific flaw exists within the CommandServlet class. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose information in the context of SYSTEM.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://us-cert.cisa.gov/ics/advisories/icsa-21-040-02

## Disclosure Timeline

- 2020-11-18 - Vulnerability reported to vendor
- 2021-02-11 - Coordinated public release of advisory
