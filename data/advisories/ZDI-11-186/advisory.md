# ZDI-11-186: Oracle Java ICC Profile Multi-Language 'curv' Tag Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-186
- **ZDI-CAN:** ZDI-CAN-1049
- **Date:** 2011-06-08
- **CVE:** CVE-2011-0862
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** Java Runtime
- **Credit:** binaryproof
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-186/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of java. Authentication is not required to exploit this vulnerability. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists within the way Java handles color profiles. When parsing a color profile containing a invalid MultiLanguage 'curv' tag it is possible to cause a memory corruption that can lead to remote code being executed under to user running the browser.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/javacpujune2011-313339.html

## Disclosure Timeline

- 2011-01-21 - Vulnerability reported to vendor
- 2011-06-08 - Coordinated public release of advisory
