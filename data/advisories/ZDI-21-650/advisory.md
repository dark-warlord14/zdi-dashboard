# ZDI-21-650: Advantech iView getInventoryReportData SQL Injection Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-650
- **ZDI-CAN:** ZDI-CAN-11834
- **Date:** 2021-06-07
- **CVE:** CVE-2021-32932
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Advantech
- **Affected Products:** iView
- **Credit:** Selim Enes Karaduman (@Enesdex)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-650/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Advantech iView. Authentication is not required to exploit this vulnerability. The specific flaw exists within the getInventoryReportData action of NetworkServlet, which listens on TCP port 8080 by default. When parsing the query element, the process does not properly validate a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to disclose information in the context of the service account.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://us-cert.cisa.gov/ics/advisories/icsa-21-154-01

## Disclosure Timeline

- 2021-01-29 - Vulnerability reported to vendor
- 2021-06-07 - Coordinated public release of advisory
