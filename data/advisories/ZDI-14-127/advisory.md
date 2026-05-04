# ZDI-14-127: Symantec Workspace Streaming Agent XMLRPC Request putFile Method Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-127
- **ZDI-CAN:** ZDI-CAN-2102
- **Date:** 2014-05-13
- **CVE:** CVE-2014-1649
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Symantec
- **Affected Products:** Symantec Workspace Streaming
- **Credit:** Andrea Micalizzi (rgod)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-127/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Symantec Workspace Streaming. Authentication is not required to exploit this vulnerability. The specific flaw exists within the SWS Agent (as_agent.exe) component. By sending a crafted XMLRPC request to this component, an attacker is able to overwrite configuration files for the Workspace Streaming server. An attacker can exploit this vulnerability to execute arbitrary code as SYSTEM.

## Additional Details

Symantec has issued an update to correct this vulnerability. More details can be found at: http://www.symantec.com/security_response/securityupdates/detail.jsp?fid=security_advisory&pvid=security_advisory&year=&suid=20140512_00

## Disclosure Timeline

- 2014-01-30 - Vulnerability reported to vendor
- 2014-05-13 - Coordinated public release of advisory
