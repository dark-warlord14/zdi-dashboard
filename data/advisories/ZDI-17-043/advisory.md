# ZDI-17-043: Advantech WebAccess updateTemplate SQL Injection Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-043
- **ZDI-CAN:** ZDI-CAN-3679
- **Date:** 2017-01-12
- **CVE:** CVE-2017-5154 , CVE-2017-5152
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/Au:S/C:P/I:P/A:P
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess
- **Credit:** Tenable Network Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-043/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Advantech WebAccess. Authentication is required to exploit this vulnerability, but can be easily bypassed. The specific flaw exists within updateTemplate.aspx. The vulnerability is caused by lack of input validation before using a remotely supplied string to construct SQL queries. An attacker can use this vulnerability to disclose passwords of administrative accounts used by Advantech WebAccess.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-17-012-01

## Disclosure Timeline

- 2016-04-12 - Vulnerability reported to vendor
- 2017-01-12 - Coordinated public release of advisory
