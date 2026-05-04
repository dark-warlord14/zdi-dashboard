# ZDI-13-071: Oracle Java t2k.dll glyph_AddPoint() Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-071
- **ZDI-CAN:** ZDI-CAN-1699
- **Date:** 2013-05-10
- **CVE:** CVE-2013-2434
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** Java Runtime
- **Credit:** Alin Rad Pop
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-071/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of the Oracle Java. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within t2k.dll glyph_AddPoint() when rendering Type1 or Type2 fonts. Memory corruption could occur when manipulating a point count in the font file. This could lead to remote code execution under the context of the process.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/javacpuapr2013-1928497.html

## Disclosure Timeline

- 2013-01-08 - Vulnerability reported to vendor
- 2013-05-10 - Coordinated public release of advisory
