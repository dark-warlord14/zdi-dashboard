# ZDI-13-247: Oracle Java FileImageInputStream Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-247
- **ZDI-CAN:** ZDI-CAN-1894
- **Date:** 2013-10-16
- **CVE:** CVE-2013-5829
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** Java Runtime
- **Credit:** Ben Murphy
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-247/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Java. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific vulnerability is inside the FileImageInputStream class. With the usage of this class, it is possible to disable the security manager and run code as privileged. This allows a malicious applet to execute attacker-supplied code resulting in remote code execution under the context of the current user.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/cpuoct2013-1899837.html

## Disclosure Timeline

- 2013-06-10 - Vulnerability reported to vendor
- 2013-10-16 - Coordinated public release of advisory
