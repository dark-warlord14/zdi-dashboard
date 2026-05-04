# ZDI-16-446: Oracle Java MethodHandles dropArguments Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-446
- **ZDI-CAN:** ZDI-CAN-3719
- **Date:** 2016-07-21
- **CVE:** CVE-2016-3598
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Oracle
- **Affected Products:** Java
- **Credit:** XOR19
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-446/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Java. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the implementation of MethodHandles' dropArguments method. Due to unsafe handling of reflection of privileged classes inside the MethodHandles class, it is possible for untrusted code to gain access to privileged methods and properties. This can result in remote code execution under the context of the current process.

## Disclosure Timeline

- 2016-04-28 - Vulnerability reported to vendor
- 2016-07-21 - Coordinated public release of advisory
