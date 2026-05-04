# ZDI-11-013: Symantec Web Gateway Management Interface USERNAME Blind SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-013
- **ZDI-CAN:** ZDI-CAN-879
- **Date:** 2011-01-12
- **CVE:** CVE-2010-0115
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Symantec
- **Affected Products:** Web Gateway
- **Credit:** RadLSneak
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-013/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Symantec Web Gateway. Authentication is not required to exploit this vulnerability. The specific flaw exists within the management interface which listens by default on TCP port 443. While parsing requests sent to the login.php page, the process does not properly sanitize the USERNAME POST parameter. By sending a specially crafted string, a remote attacker can leverage this vulnerability to inject arbitrary SQL into the backend database on the server.

## Additional Details

Symantec has issued an update to correct this vulnerability. More details can be found at: http://www.symantec.com/business/security_response/securityupdates/detail.jsp?fid=security_advisory&pvid=security_advisory&year=2011&suid=20110112_00

## Disclosure Timeline

- 2010-09-23 - Vulnerability reported to vendor
- 2011-01-12 - Coordinated public release of advisory
