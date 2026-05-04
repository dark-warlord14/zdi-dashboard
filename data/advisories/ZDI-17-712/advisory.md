# ZDI-17-712: Advantech WebAccess rmTemplate SQL Injection Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-712
- **ZDI-CAN:** ZDI-CAN-4548
- **Date:** 2017-08-30
- **CVE:** CVE-2017-12710
- **CVSS:** 9.4
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:N
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess
- **Credit:** Tenable Network Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-712/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Advantech WebAccess. Authentication is required to exploit this vulnerability, but can be easily bypassed. The specific flaw exists within rmTemplate.aspx. The vulnerability is caused by lack of input validation before using a remotely supplied string to construct SQL queries. An attacker can use this vulnerability to disclose passwords of administrative accounts used by Advantech WebAccess.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-17-241-02

## Disclosure Timeline

- 2017-03-01 - Vulnerability reported to vendor
- 2017-08-30 - Coordinated public release of advisory
