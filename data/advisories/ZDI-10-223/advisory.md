# ZDI-10-223: Symantec IM Manager Administrative Interface LoggedInUsers.lgx Definition File SQL Injection Vulnerabilities

## Metadata

- **ZDI ID:** ZDI-10-223
- **ZDI-CAN:** ZDI-CAN-871
- **Date:** 2010-10-27
- **CVE:** CVE-2010-0112
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Symantec
- **Affected Products:** IM Manager
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-223/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Symantec IM Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the rdpageimlogic.aspx and rdPage.aspx pages which is exposed through an IIS extension on the default web server port. By setting the 'rdReport' argument to the value 'LoggedInUsers' an attacker can force the server to load the LoggedInUSers.lgx definition file. This file contains multiple SQL injections within the following parameters: 'loginTimeStamp', 'dbo', 'dateDiffParam' and 'whereClause'. An attacker can abuse this to inject arbitrary SQL statements to be evaluated by the back-end database.

## Additional Details

Symantec has issued an update to correct this vulnerability. More details can be found at: http://www.symantec.com/business/security_response/securityupdates/detail.jsp?fid=security_advisory&pvid=security_advisory&year=2010&suid=20101027_01

## Disclosure Timeline

- 2010-07-20 - Vulnerability reported to vendor
- 2010-10-27 - Coordinated public release of advisory
