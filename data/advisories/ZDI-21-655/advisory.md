# ZDI-21-655: Advantech iView NetworkServlet findUpdateDeviceListDetails SQL Injection Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-655
- **ZDI-CAN:** ZDI-CAN-13137
- **Date:** 2021-06-07
- **CVE:** CVE-2021-32932
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Advantech
- **Affected Products:** iView
- **Credit:** Selim Enes Karaduman @enesdex
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-655/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Advantech iView. Authentication is not required to exploit this vulnerability. The specific flaw exists within the NetworkServlet class. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://us-cert.cisa.gov/ics/advisories/icsa-21-154-01

## Disclosure Timeline

- 2021-03-26 - Vulnerability reported to vendor
- 2021-06-07 - Coordinated public release of advisory
