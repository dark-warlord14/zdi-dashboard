# ZDI-14-104: Oracle Java permuteArguments Sandbox Bypass Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-104
- **ZDI-CAN:** ZDI-CAN-2060
- **Date:** 2014-04-21
- **CVE:** CVE-2014-0432
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** Java Runtime
- **Credit:** Ben Murphy
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-104/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Java. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the usage of permuteArguments. With the usage of this method, it is possible to disable the security manager and run code as privileged. This allows a malicious applet to execute attacker-supplied code resulting in remote code execution under the context of the current user.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/cpuapr2014-1972952.html

## Disclosure Timeline

- 2013-12-09 - Vulnerability reported to vendor
- 2014-04-21 - Coordinated public release of advisory
