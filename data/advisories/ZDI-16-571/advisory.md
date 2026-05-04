# ZDI-16-571: Oracle Java Runtime Environment java.awt.Menu Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-571
- **ZDI-CAN:** ZDI-CAN-3812
- **Date:** 2016-11-01
- **CVE:** CVE-2016-5568
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Oracle
- **Affected Products:** Java
- **Credit:** bo13oy of CloverSec Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-571/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Java. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of java.awt.Menu objects. By performing actions in code an attacker can cause a pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code outside the context of the Java sandbox.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/security-advisory/cpuoct2016-2881722.html

## Disclosure Timeline

- 2016-06-02 - Vulnerability reported to vendor
- 2016-11-01 - Coordinated public release of advisory
