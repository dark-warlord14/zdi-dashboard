# ZDI-13-067: Cisco Clean Access Manager filter SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-067
- **ZDI-CAN:** ZDI-CAN-1535
- **Date:** 2013-05-10
- **CVE:** CVE-2013-1177
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Cisco
- **Affected Products:** Clean Access Manager
- **Credit:** Nenad Stojanovski
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-067/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Cisco Clean Access Manager. Authentication is not required to exploit this vulnerability. The specific flaw is in the handling of filter URL parameters when constructing SQL database queries. By specially crafting URL parameters, it is possible to influence the SQL queries to gain remote code execution on the affected system.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: http://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20130417-nac

## Disclosure Timeline

- 2012-07-24 - Vulnerability reported to vendor
- 2013-05-10 - Coordinated public release of advisory
