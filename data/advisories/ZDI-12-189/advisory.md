# ZDI-12-189: Oracle Java WebStart Changing System Properties Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-189
- **ZDI-CAN:** ZDI-CAN-1501
- **Date:** 2012-12-21
- **CVE:** CVE-2012-1721
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** Java Runtime
- **Credit:** Chris Ries
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-189/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Java. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists because it is possible to change system properties through trusted JNLP files. If a JNLP file requests "<all-permissions/>" and only references signed, trusted JAR files, it can set all System properties. By referencing a trusted JNLP file from an untrusted one it is possible to change System Properties that can lead to remote code execution under the context of the current user.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/javacpujun2012-1515912.html

## Disclosure Timeline

- 2012-03-14 - Vulnerability reported to vendor
- 2012-12-21 - Coordinated public release of advisory
