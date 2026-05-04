# ZDI-11-305: Oracle Java Applet Rhino Script Engine Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-305
- **ZDI-CAN:** ZDI-CAN-1254
- **Date:** 2011-10-26
- **CVE:** CVE-2011-3544
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** Java Runtime
- **Credit:** Michael Schierl
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-305/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Java. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the way Java handles Rhino Javascript errors. The built-in javascript engine in Java fails to perform sufficient sanitation on javascript error objects. The effect is that untrusted code can run in privileged context. This can result in remote code execution under the context of the current user.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/javacpuoct2011-443431.html

## Disclosure Timeline

- 2011-05-12 - Vulnerability reported to vendor
- 2011-10-26 - Coordinated public release of advisory
