# ZDI-14-077: Advantech WebAccess DBVisitor.dll SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-077
- **ZDI-CAN:** ZDI-CAN-1938
- **Date:** 2014-04-10
- **CVE:** CVE-2014-0763
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Advantech
- **Affected Products:** Advantech WebAccess
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-077/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Advantech WebAccess. Authentication is not required to exploit this vulnerability. The specific flaw exists within the DBVisitor.dll component. Multiple SOAP requests implemented by the component are vulnerable to SQL Injection. These flaws allow an attacker to execute arbitrary SQL statements in the context of the web service and to exfiltrate data (including the account names and password hashes) from the vulnerable product.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-14-079-03

## Disclosure Timeline

- 2014-01-05 - Vulnerability reported to vendor
- 2014-04-10 - Coordinated public release of advisory
