# ZDI-12-038: Oracle Java JavaFX Arbitrary Argument Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-038
- **ZDI-CAN:** ZDI-CAN-1453
- **Date:** 2012-02-22
- **CVE:** N/A
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Oracle
- **Affected Products:** Java Runtime
- **Credit:** Chris Ries
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-038/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Java. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within JavaFX, a downloadable Java extension. The JavaFX Jar file is signed by Oracle and can be installed without user interaction. Once installed it is possible to invoke the main method of any trusted class with arbitrary arguments and with a trusted call stack. This can be leveraged to remote code execution under the context of the user.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/javacpufeb2012-366318.html

## Disclosure Timeline

- 2011-11-21 - Vulnerability reported to vendor
- 2012-02-22 - Coordinated public release of advisory
