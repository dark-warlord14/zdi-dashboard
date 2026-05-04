# ZDI-18-487: Advantech WebAccess Node Quality_Reg ItemIdAry SQL Injection Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-487
- **ZDI-CAN:** ZDI-CAN-5651
- **Date:** 2018-05-18
- **CVE:** CVE-2018-7501
- **CVSS:** 5.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess Node
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-487/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Advantech WebAccess Node. Authentication is not required to exploit this vulnerability. The specific flaw exists within Quality_Reg.asp. When parsing the ItemIdAry parameter, the process does not properly validate a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to disclose sensitive information under the context of the database.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-18-135-01

## Disclosure Timeline

- 2018-02-09 - Vulnerability reported to vendor
- 2018-05-18 - Coordinated public release of advisory
- 2018-05-18 - Advisory Updated
