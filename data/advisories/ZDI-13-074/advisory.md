# ZDI-13-074: Oracle Java JavaFX WebPage Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-074
- **ZDI-CAN:** ZDI-CAN-1727
- **Date:** 2013-05-10
- **CVE:** CVE-2013-2428
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** Java Runtime
- **Credit:** Vitaliy Toropov
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-074/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Java. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the JavaFX WebPage class. A descendant class can overwrite the getPage method with a custom pointer into the native function. This could lead to remote code execution under the context of the process.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/javacpuapr2013-1928497.html

## Disclosure Timeline

- 2013-01-07 - Vulnerability reported to vendor
- 2013-05-10 - Coordinated public release of advisory
