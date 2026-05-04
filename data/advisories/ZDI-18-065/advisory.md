# ZDI-18-065: Advantech WebAccess BWSCADASoap Login Method SQL Injection Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-065
- **ZDI-CAN:** ZDI-CAN-5407
- **Date:** 2018-01-05
- **CVE:** CVE-2017-16716
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-065/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on vulnerable installations of Advantech WebAccess. The specific flaw exists within processing of the Login method of the BWSCADASoap entry point. When parsing the ProjectName and Username elements, the process does not properly validate user-supplied strings before using them to construct SQL queries. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the database.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-18-004-02

## Disclosure Timeline

- 2017-12-01 - Vulnerability reported to vendor
- 2018-01-05 - Coordinated public release of advisory
