# ZDI-13-010: Oracle Java PV_ProcessSampleWithSMOD Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-010
- **ZDI-CAN:** ZDI-CAN-1534
- **Date:** 2013-02-11
- **CVE:** CVE-2013-1481
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Oracle
- **Affected Products:** Java Runtime
- **Credit:** Aniway.Anyway@gmail.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-010/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Java. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the way the Java sound libraries parse Soundbank files. Due to an signed comparison check, it is possible to cause an out of bound read on an array of function pointers. This could lead to remote code execution under the context of the process.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/javacpufeb2013-1841061.html

## Disclosure Timeline

- 2012-10-29 - Vulnerability reported to vendor
- 2013-02-11 - Coordinated public release of advisory
