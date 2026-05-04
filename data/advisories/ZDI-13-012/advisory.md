# ZDI-13-012: Oracle Java JavaFX WCGraphicsManager Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-012
- **ZDI-CAN:** ZDI-CAN-1725
- **Date:** 2013-02-11
- **CVE:** CVE-2012-1543
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Oracle
- **Affected Products:** Java Runtime
- **Credit:** Vitaliy Toropov
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-012/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Java. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the JavaFX WCGraphicsManager class. This class exposes methods that result in calls to the append() native function. One of the arguments passed to this native function is interpreted as a pointer to an object. This can be leveraged by an attacker to gain remote code execution under the context of the process.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/javacpufeb2013-1841061.html

## Disclosure Timeline

- 2013-01-07 - Vulnerability reported to vendor
- 2013-02-11 - Coordinated public release of advisory
