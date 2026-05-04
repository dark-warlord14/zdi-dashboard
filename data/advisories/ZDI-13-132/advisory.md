# ZDI-13-132: Oracle Java KeyStore SecurityManager Bypass Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-132
- **ZDI-CAN:** ZDI-CAN-1730
- **Date:** 2013-06-27
- **CVE:** N/A
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Oracle
- **Affected Products:** Java Runtime
- **Credit:** Ben Murphy
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-132/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Java. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the java.security.KeyStore class. The issue lies in the execution of a user-supplied callback in a privileged context. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/javacpujun2013-1899847.html

## Disclosure Timeline

- 2013-02-22 - Vulnerability reported to vendor
- 2013-06-27 - Coordinated public release of advisory
