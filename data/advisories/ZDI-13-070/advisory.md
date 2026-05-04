# ZDI-13-070: Oracle Java mort TTF Table Ligature Substitution Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-070
- **ZDI-CAN:** ZDI-CAN-1697
- **Date:** 2013-05-10
- **CVE:** CVE-2013-2383
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** Java Runtime
- **Credit:** Alin Rad Pop
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-070/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of the Oracle Java. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the fontmanager native component. There is a vulnerability when processing Ligature Substitution subtables embedded in a "mort" table, which can result in a memory corruption. This allows a malicious applet to execute attacker-supplied code resulting in remote code execution under the context of the current user.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/javacpuapr2013-1928497.html

## Disclosure Timeline

- 2012-12-10 - Vulnerability reported to vendor
- 2013-05-10 - Coordinated public release of advisory
