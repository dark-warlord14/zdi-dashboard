# ZDI-14-298: CSWorks Software Framework SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-298
- **ZDI-CAN:** ZDI-CAN-2191
- **Date:** 2014-08-27
- **CVE:** CVE-2014-2351
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** CSWorks
- **Affected Products:** CSWorks
- **Credit:** John Leitch
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-298/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of CSWorks. Authentication is not required to exploit this vulnerability. The specific flaw exists within the data source templating. CSWorks does not properly sanitize or validate the data used to construct read and write paths which can lead to SQL injection. An attacker may be able to leverage this vulnerability to achieve remote code execution.

## Additional Details

CSWorks has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-14-135-01

## Disclosure Timeline

- 2014-04-23 - Vulnerability reported to vendor
- 2014-08-27 - Coordinated public release of advisory
