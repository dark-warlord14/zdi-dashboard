# ZDI-13-245: Oracle Java NumberFormatter and RealTimeSequencer Sandbox Bypass Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-245
- **ZDI-CAN:** ZDI-CAN-1878
- **Date:** 2013-10-16
- **CVE:** CVE-2013-5783
- **CVSS:** 5.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:N
- **Affected Vendors:** Oracle
- **Affected Products:** Java Runtime
- **Credit:** Ben Murphy
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-245/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Java. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the usage of NumberFormatter and RealTimeSequencer. With the usage of these classes, it is possible to disable the security manager and run code as privileged. This allows a malicious applet to execute attacker-supplied code resulting in remote code execution under the context of the current user.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/cpuoct2013-1899837.html

## Disclosure Timeline

- 2013-05-14 - Vulnerability reported to vendor
- 2013-10-16 - Coordinated public release of advisory
