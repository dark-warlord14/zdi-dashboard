# ZDI-10-221: Symantec IM Manager Administrative Interface IMAdminReportTrendFormRun.asp SQL Injection Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-221
- **ZDI-CAN:** ZDI-CAN-773
- **Date:** 2010-10-27
- **CVE:** CVE-2010-0112
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Symantec
- **Affected Products:** IM Manager
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-221/
## Vulnerability Details

This vulnerability allows remote attackers to inject arbitrary SQL into the packaged database on vulnerable installations of Symantec IM Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Administrative interface installed with IM Manager. While there is authentication on the main page of the installed IIS extension, many of the pages can be accessed directly. One of these pages, IMAdminReportTrendFormRun.asp, is vulnerable to a SQL injection vulnerability. The ASP code lacks sanity checks on the 'groupList' parameter. Thus, an attacker can abuse this to inject arbitrary SQL into the backend database.

## Additional Details

Symantec has issued an update to correct this vulnerability. More details can be found at: http://www.symantec.com/business/security_response/securityupdates/detail.jsp?fid=security_advisory&pvid=security_advisory&year=2010&suid=20101027_01

## Disclosure Timeline

- 2010-04-08 - Vulnerability reported to vendor
- 2010-10-27 - Coordinated public release of advisory
