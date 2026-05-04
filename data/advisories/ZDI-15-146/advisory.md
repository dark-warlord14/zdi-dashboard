# ZDI-15-146: Oracle Endeca Tools and Frameworks Script.action Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-146
- **ZDI-CAN:** ZDI-CAN-2660
- **Date:** 2015-04-16
- **CVE:** CVE-2015-0495
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Oracle
- **Affected Products:** Endeca Tools and Frameworks
- **Credit:** Steven Seeley of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-146/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Endeca Tools and Frameworks. Authentication is required to exploit this vulnerability, but authentication is easily bypassed. This product installs a web application called Oracle Endeca Workbench, which includes a handler for requests to Script.action. This handler fails to properly authenticate the user, so that an attacker can access this handler using the built-in and undocumented "anonymous" user account. This handler allows an attacker to specify arbitrary code that will execute on the Endeca Tools and Frameworks installation, under the context of the "endeca" user.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/cpuapr2015-2365600.html

## Disclosure Timeline

- 2014-12-23 - Vulnerability reported to vendor
- 2015-04-16 - Coordinated public release of advisory
