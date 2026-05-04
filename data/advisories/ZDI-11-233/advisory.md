# ZDI-11-233: Symantec Web Gateway forget.php SQL Injection Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-233
- **ZDI-CAN:** ZDI-CAN-1048
- **Date:** 2011-07-07
- **CVE:** CVE-2011-0549
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Symantec
- **Affected Products:** Web Gateway
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-233/
## Vulnerability Details

This vulnerability allows remote attackers to inject arbitrary SQL on vulnerable installations of the Symantec Web Gateway appliance. Authentication is not required to exploit this vulnerability. The specific flaw exists within the username parameter of POST requests to the forget.php script. The parameter is not sanitized and a remote attacker can abuse this to inject arbitrary SQL into the underlying database.

## Additional Details

Symantec has issued an update to correct this vulnerability. More details can be found at: http://www.symantec.com/business/security_response/securityupdates/detail.jsp?fid=security_advisory&pvid=security_advisory&year=2011&suid=20110707_00

## Disclosure Timeline

- 2011-04-01 - Vulnerability reported to vendor
- 2011-07-07 - Coordinated public release of advisory
