# ZDI-12-197: Oracle Java java.beans.Statement Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-197
- **ZDI-CAN:** ZDI-CAN-1590
- **Date:** 2012-12-21
- **CVE:** CVE-2012-1682
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** Java Runtime
- **Credit:** James Forshaw (tyranid)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-197/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Java. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the java.beans.Expression class. Due to unsafe handling of reflection of privileged classes inside the Expression class it is possible for untrusted code to gain access to privileged methods and properties. This can result in remote code execution under the context of the current process.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/alert-cve-2012-4681-1835715.html

## Disclosure Timeline

- 2012-07-24 - Vulnerability reported to vendor
- 2012-12-21 - Coordinated public release of advisory
