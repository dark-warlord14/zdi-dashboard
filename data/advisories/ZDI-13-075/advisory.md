# ZDI-13-075: Oracle Java java.util.concurrent.ConcurrentHashMap Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-075
- **ZDI-CAN:** ZDI-CAN-1731
- **Date:** 2013-05-10
- **CVE:** CVE-2013-2426
- **CVSS:** 9.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** Java Runtime
- **Credit:** Ben Murphy
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-075/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Java. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the java.util.concurrent.ConcurrentHashMap class. The issue lies in segmentShift and segmentMask fields which can be used to manipulate memory outside of the allocated buffer. An attacker can leverage this vulnerability to execute code under the context of the current user.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/javacpuapr2013-1928497.html

## Disclosure Timeline

- 2013-02-22 - Vulnerability reported to vendor
- 2013-05-10 - Coordinated public release of advisory
