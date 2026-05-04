# ZDI-18-553: Advantech WebAccess Node BWSCADASoap GetNodeList SQL Injection Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-553
- **ZDI-CAN:** ZDI-CAN-5590
- **Date:** 2018-06-08
- **CVE:** CVE-2018-7501
- **CVSS:** 4.0
- **CVSS Vector:** AV:N/AC:L/Au:S/C:P/I:N/A:N
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess Node
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-553/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Advantech WebAccess Node. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the handling of the GetNodeList function in BWMobileService.dll. When parsing the ProjectName parameter, the process does not properly validate a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to disclose sensitive information under the context of the database.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-18-135-01

## Disclosure Timeline

- 2018-01-19 - Vulnerability reported to vendor
- 2018-06-08 - Coordinated public release of advisory
- 2018-06-08 - Advisory Updated
