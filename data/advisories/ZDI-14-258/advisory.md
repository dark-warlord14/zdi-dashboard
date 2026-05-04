# ZDI-14-258: Oracle Java ResourceBundle Format String Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-258
- **ZDI-CAN:** ZDI-CAN-2246
- **Date:** 2014-07-18
- **CVE:** CVE-2014-2490
- **CVSS:** 9.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** Java Runtime
- **Credit:** John Leitch
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-258/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Java. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of ResourceBundles. The issue lies in insufficient validation of user-supplied data when applying a ResourceBundle. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/cpujul2014-1972956.html

## Disclosure Timeline

- 2014-04-03 - Vulnerability reported to vendor
- 2014-07-18 - Coordinated public release of advisory
