# ZDI-13-002: Oracle Java Runtime Environment MethodHandle Security Manager Bypass Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-002
- **ZDI-CAN:** ZDI-CAN-1693
- **Date:** 2013-02-01
- **CVE:** CVE-2012-3174
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Oracle
- **Affected Products:** Java Runtime
- **Credit:** Ben Murphy
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-002/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of the Oracle Java Runtime Environment. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific bypass exists within usage of MethodHandle to the invoke method in the sun.misc.reflect.Trampoline class. This allows a malicious applet to execute attacker supplied code resulting in remote code execution under the context of the current user.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/alert-cve-2013-0422-1896849.html

## Disclosure Timeline

- 2012-12-10 - Vulnerability reported to vendor
- 2013-02-01 - Coordinated public release of advisory
