# ZDI-10-203: Oracle Sun Java ICC Profile Unicode Description Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-203
- **ZDI-CAN:** ZDI-CAN-802
- **Date:** 2010-10-12
- **CVE:** CVE-2010-3571
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Sun Microsystems
- **Affected Products:** Java Runtime
- **Credit:** Intevydis http://intevydis.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-203/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle's Java Runtime Environment. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists within the implementation of the color profile parser. When processing a particular Tag structure out of a color profile, the parser will read a 32-bit integer and use it to calculate the size for a memory allocation. Due to the result being larger than 32 bits, an integer overflow will occur. This will lead to code execution under the context of the application.

## Additional Details

Sun Microsystems has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/javacpuoct2010-176258.html

## Disclosure Timeline

- 2010-06-30 - Vulnerability reported to vendor
- 2010-10-12 - Coordinated public release of advisory
