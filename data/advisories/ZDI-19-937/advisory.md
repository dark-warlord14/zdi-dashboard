# ZDI-19-937: Advantech WISE-PaaS/RMM SQLMgmt qryData SQL Injection Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-937
- **ZDI-CAN:** ZDI-CAN-9148
- **Date:** 2019-11-01
- **CVE:** CVE-2019-18229
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Advantech
- **Affected Products:** WISE-PaaS/RMM
- **Credit:** rgod of 9sg
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-937/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Advantech WISE-PasS/RMM. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the SQLMgmt class. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to disclose information in the context of the Postgres database.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://www.us-cert.gov/ics/advisories/icsa-19-304-01

## Disclosure Timeline

- 2019-08-20 - Vulnerability reported to vendor
- 2019-11-01 - Coordinated public release of advisory
