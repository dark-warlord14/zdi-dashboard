# ZDI-10-226: Symantec IM Manager rdServer.dll sGetDefinition SQL Injection Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-226
- **ZDI-CAN:** ZDI-CAN-943
- **Date:** 2010-10-27
- **CVE:** CVE-2010-0112
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Symantec
- **Affected Products:** IM Manager
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-226/
## Vulnerability Details

This vulnerability allows remote attackers to inject arbitrary SQL into the backend database on vulnerable installations of Symantec IM Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the IM Manager interface exposed by the web server which listens by default on TCP port 80. The rdpageimlogic.aspx file does not validate the rdReport variable when parsing requests. It parses SQL statements from the file pointed to by this variable. A remote attacker can abuse this behavior to inject arbitrary SQL into the backend database.

## Additional Details

Symantec has issued an update to correct this vulnerability. More details can be found at: http://www.symantec.com/business/security_response/securityupdates/detail.jsp?fid=security_advisory&pvid=security_advisory&year=2010&suid=20101027_01

## Disclosure Timeline

- 2010-09-24 - Vulnerability reported to vendor
- 2010-10-27 - Coordinated public release of advisory
