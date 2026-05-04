# ZDI-20-417: Advantech WebAccess/NMS DBUtil SQL Injection Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-417
- **ZDI-CAN:** ZDI-CAN-9777
- **Date:** 2020-04-08
- **CVE:** CVE-2020-10617
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess/NMS
- **Credit:** rgod of 9sg
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-417/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Advantech WebAccess/NMS. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of calls to the getManagedDeviceByIP method of the DBUtil class. When parsing the deviceIP parameter of the upgBkpResults endpoint, the process does not properly validate a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to disclose files in the context of SYSTEM.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://www.us-cert.gov/ics/advisories/icsa-20-098-01

## Disclosure Timeline

- 2019-12-03 - Vulnerability reported to vendor
- 2020-04-08 - Coordinated public release of advisory
