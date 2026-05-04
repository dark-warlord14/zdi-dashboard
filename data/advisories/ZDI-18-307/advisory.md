# ZDI-18-307: Oracle Java MethodHandles tryFinally Type Confusion Sandbox Escape Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-307
- **ZDI-CAN:** ZDI-CAN-5505
- **Date:** 2018-04-18
- **CVE:** CVE-2018-2826
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Oracle
- **Affected Products:** Java
- **Credit:** XOR19
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-307/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Java. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the implementation of the tryFinally method in the MethodHandles class. Due to unsafe handling of reflection of privileged classes inside the MethodHandles class, it is possible for untrusted code to gain access to privileged methods and properties. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/security-advisory/cpuapr2018-3678067.html

## Disclosure Timeline

- 2017-12-19 - Vulnerability reported to vendor
- 2018-04-18 - Coordinated public release of advisory
- 2018-04-18 - Advisory Updated
