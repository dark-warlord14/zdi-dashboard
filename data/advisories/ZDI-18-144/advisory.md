# ZDI-18-144: Advantech WebAccess Node uMailLogin Proj SQL Injection Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-144
- **ZDI-CAN:** ZDI-CAN-5503
- **Date:** 2018-02-06
- **CVE:** CVE-2018-5443
- **CVSS:** 5.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess Node
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-144/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Advantech WebAccess Node. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of the ProjName parameter in uMailLogin.asp. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to disclose sensitive information under the context of the database.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-18-023-01

## Disclosure Timeline

- 2017-12-19 - Vulnerability reported to vendor
- 2018-02-06 - Coordinated public release of advisory
- 2018-02-06 - Advisory Updated
