# ZDI-13-011: Oracle Java NativeJavaConstructor Class Serialization Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-011
- **ZDI-CAN:** ZDI-CAN-1587
- **Date:** 2013-02-11
- **CVE:** CVE-2012-3213
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Oracle
- **Affected Products:** Java Runtime
- **Credit:** James Forshaw (tyranid)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-011/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Java. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists due to insufficient checks during deserialization in the NativeJavaConstructor class that is part of the Rhino JavaScript Engine. This allows for the construction of otherwise privileged objects which can lead to remote code execution under the context of the current user.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/javacpufeb2013-1841061.html

## Disclosure Timeline

- 2012-07-24 - Vulnerability reported to vendor
- 2013-02-11 - Coordinated public release of advisory
