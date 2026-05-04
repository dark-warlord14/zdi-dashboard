# ZDI-17-056: Oracle Java AtomicReferenceFieldUpdater Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-056
- **ZDI-CAN:** ZDI-CAN-3834
- **Date:** 2017-01-24
- **CVE:** CVE-2017-3272
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Oracle
- **Affected Products:** Java
- **Credit:** XOR19
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-056/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Java. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the AtomicReferenceFieldUpdater class. Due to insufficient type checking involving this class, it is possible for untrusted code to gain access to privileged methods and properties. An attacker can leverage this vulnerability to execute code under the context of the process.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/security-advisory/cpujan2017-2881727.html

## Disclosure Timeline

- 2016-08-30 - Vulnerability reported to vendor
- 2017-01-24 - Coordinated public release of advisory
