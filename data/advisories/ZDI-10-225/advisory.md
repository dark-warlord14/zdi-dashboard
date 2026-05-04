# ZDI-10-225: Symantec IM Manager Administrative Interface DetailReportGroup.lgx Definition File SQL Injection Vulnerabilities

## Metadata

- **ZDI ID:** ZDI-10-225
- **ZDI-CAN:** ZDI-CAN-873
- **Date:** 2010-10-27
- **CVE:** CVE-2010-0112
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Symantec
- **Affected Products:** IM Manager
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-225/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Symantec IM Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the rdPageImlogic.aspx page which is exposed through an IIS extension on the default web server port. By setting the 'rdReport' argument to the value 'DetailReportGroup' an attacker can force the server to load the DetailReportGroup.lgx definition file. This file contains SQL injections within multiple parameters. An attacker can abuse this to inject arbitrary SQL statements to be evaluated by the back-end database.

## Additional Details

Symantec has issued an update to correct this vulnerability. More details can be found at: http://www.symantec.com/business/security_response/securityupdates/detail.jsp?fid=security_advisory&pvid=security_advisory&year=2010&suid=20101027_01

## Disclosure Timeline

- 2010-07-20 - Vulnerability reported to vendor
- 2010-10-27 - Coordinated public release of advisory
