# ZDI-17-999: Ecava IntegraXor Report batchlist SQL Injection Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-999
- **ZDI-CAN:** ZDI-CAN-5385
- **Date:** 2017-12-20
- **CVE:** CVE-2017-16733
- **CVSS:** 5.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Ecava
- **Affected Products:** IntegraXor
- **Credit:** Steven Seeley of Source Incite Michael DePlante and Brad Taylor
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-999/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Ecava IntegraXor. Authentication is not required to exploit this vulnerability. The specific flaw exists within the batchlist report page. When parsing the 'to' parameter, the process does not properly validate a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to disclose sensitive information under the context of the current process.

## Additional Details

Ecava has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-17-353-03

## Disclosure Timeline

- 2017-11-24 - Vulnerability reported to vendor
- 2017-12-20 - Coordinated public release of advisory
