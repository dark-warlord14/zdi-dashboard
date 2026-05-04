# ZDI-13-072: Oracle Java t2k Type1 Subroutine Indexing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-072
- **ZDI-CAN:** ZDI-CAN-1700
- **Date:** 2013-05-10
- **CVE:** CVE-2013-2394
- **CVSS:** 9.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** Java Runtime
- **Credit:** Alin Rad Pop
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-072/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of the Oracle Java. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of Type1 fonts in t2k.dll. A file parsing vulnerability can occur by controlling a value placed after the "/Subrs" keyword in the eexec portion of the file which defines a size of an array. An attacker can leverage this to gain code execution under the context of the current user.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/javacpuapr2013-1928497.html

## Disclosure Timeline

- 2012-12-10 - Vulnerability reported to vendor
- 2013-05-10 - Coordinated public release of advisory
