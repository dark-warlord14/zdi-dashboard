# ZDI-20-378: Advantech WebAccess/NMS saveBackground SQL Injection Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-378
- **ZDI-CAN:** ZDI-CAN-9571
- **Date:** 2020-04-08
- **CVE:** CVE-2020-10617
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess/NMS
- **Credit:** rgod of 9sg
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-378/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Advantech WebAccess/NMS. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of calls to the saveBackground.action endpoint. When parsing the oldImage parameter, the process does not properly validate a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://www.us-cert.gov/ics/advisories/icsa-20-098-01

## Disclosure Timeline

- 2019-11-20 - Vulnerability reported to vendor
- 2020-04-08 - Coordinated public release of advisory
