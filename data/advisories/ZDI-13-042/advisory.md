# ZDI-13-042: Oracle Java setUncaughtExceptionHandler Security Manager Bypass Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-042
- **ZDI-CAN:** ZDI-CAN-1732
- **Date:** 2013-03-22
- **CVE:** CVE-2013-1484
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Oracle
- **Affected Products:** Java Runtime
- **Credit:** Ben Murphy
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-042/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Java. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within java.lang.Thread's setUncaughtExceptionHandler method allowing for a callback to be run with using the JDK's access control context. This allows a malicious applet to execute attacker supplied code resulting in remote code execution under the context of the process.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/javacpufeb2013update-1905892.html

## Disclosure Timeline

- 2013-01-07 - Vulnerability reported to vendor
- 2013-03-22 - Coordinated public release of advisory
