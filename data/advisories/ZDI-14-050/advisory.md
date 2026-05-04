# ZDI-14-050: McAfee Cloud Identity Manager ExtensionAccessServlet Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-050
- **ZDI-CAN:** ZDI-CAN-1929
- **Date:** 2014-04-03
- **CVE:** N/A
- **CVSS:** 7.8
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:N/A:N
- **Affected Vendors:** McAfee
- **Affected Products:** Cloud Identity Manager
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-050/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of McAfee Cloud Identify Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within a servlet called ExtensionAccessServlet which contains a directory traversal vulnerability inside the path info string of a GET request. A remote attacker can leverage this vulnerability to read arbitrary files from the underlying OS with SYSTEM privileges.

## Additional Details

McAfee has issued an update to correct this vulnerability. More details can be found at: https://kc.mcafee.com/corporate/index?page=content&id=SB10066

## Disclosure Timeline

- 2013-09-30 - Vulnerability reported to vendor
- 2014-04-03 - Coordinated public release of advisory
