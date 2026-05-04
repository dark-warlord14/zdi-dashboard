# ZDI-12-145: Symantec Endpoint Protection SemSvc.exe AgentServlet Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-145
- **ZDI-CAN:** ZDI-CAN-1357
- **Date:** 2012-08-22
- **CVE:** CVE-2012-0289
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Symantec
- **Affected Products:** Endpoint Protection
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-145/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Symantec Endpoint Protection. Authentication is not required to exploit this vulnerability. The specific flaw exists within SemSvc.exe which listens by default on TCP port 8443 (https). The SemSvc service exposes a servlet called 'AgentServlet" which allows remote users to activate certain tasks without prior authentication. In doing so, it is vulnerable to directory traversal attacks and arbitrary file deletion. When certain files are deleted, the eval() method will allow for executing user supplied commands. An attacker can leverage these vulnerabilities to execute code under the context of the SYSTEM.

## Additional Details

Symantec has issued an update to correct this vulnerability. More details can be found at: http://www.symantec.com/security_response/securityupdates/detail.jsp?fid=security_advisory&pvid=security_advisory&year=2012&suid=20120522_01

## Disclosure Timeline

- 2011-10-28 - Vulnerability reported to vendor
- 2012-08-22 - Coordinated public release of advisory
