# ZDI-11-137: Oracle Application Server Authentication Bypass Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-137
- **ZDI-CAN:** ZDI-CAN-930
- **Date:** 2011-04-19
- **CVE:** CVE-2011-0807
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** Application Server
- **Credit:** Jason Bowes
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-137/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle GlassFish Application Server and Oracle Java Application Server. Authentication is not required to exploit this vulnerability. The flaw exists within the Web Administration component which listens by default on TCP port 4848. When handling a malformed GET request to the administrative interface, the application does not properly handle an exception allowing the request to proceed without authentication. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the application.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/cpuapr2011-301950.html

## Disclosure Timeline

- 2010-09-23 - Vulnerability reported to vendor
- 2011-04-19 - Coordinated public release of advisory
