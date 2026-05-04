# ZDI-13-158: Oracle Java AWT Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-158
- **ZDI-CAN:** ZDI-CAN-1820
- **Date:** 2013-06-27
- **CVE:** CVE-2013-2470
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** Java Runtime
- **Credit:** Vitaliy Toropov
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-158/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Java. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific vulnerability is an array indexing flaw inside the Java AWT imaging library allowing for memory corruption. An attacker could leverage this vulnerability into remote execution of arbitrary code as the current user.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/javacpujun2013-1899847.html

## Disclosure Timeline

- 2013-03-29 - Vulnerability reported to vendor
- 2013-06-27 - Coordinated public release of advisory
