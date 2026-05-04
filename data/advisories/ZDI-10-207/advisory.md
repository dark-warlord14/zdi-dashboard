# ZDI-10-207: Oracle Java ActiveX Plugin Uninitialized Window Handle Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-207
- **ZDI-CAN:** ZDI-CAN-792
- **Date:** 2010-10-12
- **CVE:** CVE-2010-3555
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** Java Runtime
- **Credit:** Anonymous Stephen Fewer of Harmony Security (www.harmonysecurity.com)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-207/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle's Java platform that utilize the ActiveX Plugin. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within how the plugin initializes objects. While the plugin is in a particular state, the application will fail to initialize a field that is used as a window handle. Exploitation can lead to code execution under the privileges of the application.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/javacpuoct2010-176258.html

## Disclosure Timeline

- 2010-06-01 - Vulnerability reported to vendor
- 2010-10-12 - Coordinated public release of advisory
