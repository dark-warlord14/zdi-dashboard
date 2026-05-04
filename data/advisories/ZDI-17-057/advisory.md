# ZDI-17-057: Oracle Java Uninitialized Memory Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-057
- **ZDI-CAN:** ZDI-CAN-4018
- **Date:** 2017-01-24
- **CVE:** CVE-2017-3289
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Oracle
- **Affected Products:** Java
- **Credit:** XOR19
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-057/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Java. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the creation of an object without proper initialization. Due to this uninitialized memory, it is possible for untrusted code to gain access to privileged methods and properties. An attacker can leverage this vulnerability to execute code under the context of the process.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/security-advisory/cpujan2017-2881727.html

## Disclosure Timeline

- 2016-09-27 - Vulnerability reported to vendor
- 2017-01-24 - Coordinated public release of advisory
