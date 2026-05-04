# ZDI-13-023: Oracle Java JavaFX D3DRendererDelegate Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-023
- **ZDI-CAN:** ZDI-CAN-1594
- **Date:** 2013-02-11
- **CVE:** CVE-2013-1479
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Oracle
- **Affected Products:** Java Runtime
- **Credit:** Chris Ries
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-023/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Java. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the JavaFX D3DRendererDelegate class. A value utilized by the class constructor is passed to a native function and is interpreted as a pointer to an object. An attacker could leverage this to gain remote code execution under the context of the process.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/javacpufeb2013-1841061.html

## Disclosure Timeline

- 2012-10-29 - Vulnerability reported to vendor
- 2013-02-11 - Coordinated public release of advisory
