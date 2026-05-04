# ZDI-14-382: Oracle Java jp2launcher.exe Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-382
- **ZDI-CAN:** ZDI-CAN-2535
- **Date:** 2014-11-19
- **CVE:** CVE-2014-6466
- **CVSS:** 4.6
- **CVSS Vector:** AV:L/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Oracle
- **Affected Products:** Java Runtime
- **Credit:** Yuki Chen of Qihoo
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-382/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Java. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of paths within jp2launcher.exe. The issue lies in assumptions made in preparation for the call to java.exe. An attacker can leverage this vulnerability to execute code as the current user with medium integrity.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/cpuoct2014-1972960.html

## Disclosure Timeline

- 2014-10-06 - Vulnerability reported to vendor
- 2014-11-19 - Coordinated public release of advisory
