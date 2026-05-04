# ZDI-13-040: Oracle Java Proxy.newProxyInstance Security Manager Bypass Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-040
- **ZDI-CAN:** ZDI-CAN-1706
- **Date:** 2013-03-22
- **CVE:** CVE-2013-1484
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Oracle
- **Affected Products:** Java Runtime
- **Credit:** Ben Murphy
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-040/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of the Oracle Java. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or run a malicious file. The specific bypass of security permissions is possible via invocation of Proxy.newProxyInstance. It is possible to run user callbacks that don't have higher privileges as privileged. This allows a malicious applet to execute attacker-supplied code resulting in remote code execution under the context of the current user.

## Additional Details

http://www.oracle.com/technetwork/topics/security/javacpufeb2013update-1905892.html

## Disclosure Timeline

- 2012-12-10 - Vulnerability reported to vendor
- 2013-03-22 - Coordinated public release of advisory
