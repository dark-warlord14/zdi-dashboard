# ZDI-13-078: (Pwn2Own) Oracle Java Font Handling Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-078
- **ZDI-CAN:** ZDI-CAN-1829
- **Date:** 2013-05-10
- **CVE:** CVE-2013-1491
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** Java Runtime
- **Credit:** Joshua J. Drake with Accuvant Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-078/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Java. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of CFF-based OpenType fonts. The issue lies in two operators that allow for reading and writing elements beyond the allocated buffers. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/javacpuapr2013-1928497.html

## Disclosure Timeline

- 2013-03-29 - Vulnerability reported to vendor
- 2013-05-10 - Coordinated public release of advisory
