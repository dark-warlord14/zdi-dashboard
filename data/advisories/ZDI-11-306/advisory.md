# ZDI-11-306: Oracle Java IIOP Deserialization Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-306
- **ZDI-CAN:** ZDI-CAN-1253
- **Date:** 2011-10-26
- **CVE:** CVE-2011-3521
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** Java Runtime
- **Credit:** Sami Koivu
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-306/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Java. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the way Java handles IIOP deserialization. Due to insufficient type checking it is possible to trick java into allowing access to otherwise protected and private fields in built-in objects. This could be used, for example, to disable to security manager normally in place for applets. This leads to remote code execution under the context of the current user.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/javacpuoct2011-443431.html

## Disclosure Timeline

- 2011-05-12 - Vulnerability reported to vendor
- 2011-10-26 - Coordinated public release of advisory
