# ZDI-15-162: ManageEngine Applications Manager FailOverHelperServlet Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-162
- **ZDI-CAN:** ZDI-CAN-2427
- **Date:** 2015-04-29
- **CVE:** CVE-2014-7863
- **CVSS:** 7.8
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:N/A:N
- **Affected Vendors:** ManageEngine
- **Affected Products:** Applications Manager
- **Credit:** Andrea Micalizzi (rgod)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-162/
## Vulnerability Details

This vulnerability allows remote attackers to disclose files on vulnerable installations of ManageEngine Applications Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of the FailOverHelperServlet servlet. The issue lies in the failure to properly sanitize a filename. A remote attacker can exploit this vulnerability to disclose files from the system.

## Additional Details

ManageEngine has issued an update to correct this vulnerability. More details can be found at: https://support.zoho.com/portal/manageengine/helpcenter/articles/vulnerabilities-in-failoverhelperservlet

## Disclosure Timeline

- 2014-08-18 - Vulnerability reported to vendor
- 2015-04-29 - Coordinated public release of advisory
