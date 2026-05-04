# ZDI-13-157: Oracle Java CMMImageLayout Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-157
- **ZDI-CAN:** ZDI-CAN-1844
- **Date:** 2013-06-27
- **CVE:** CVE-2013-2464
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** Java Runtime
- **Credit:** Vitaliy Toropov
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-157/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Java. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the CMMImageLayout class. The issue lies in the failure to validate every element of the data offsets array. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/javacpujun2013-1899847.html

## Disclosure Timeline

- 2013-04-16 - Vulnerability reported to vendor
- 2013-06-27 - Coordinated public release of advisory
