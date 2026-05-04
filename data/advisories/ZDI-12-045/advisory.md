# ZDI-12-045: Oracle Java JOGL NEWT Reflection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-045
- **ZDI-CAN:** ZDI-CAN-1490
- **Date:** 2012-03-20
- **CVE:** N/A
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** Java Runtime
- **Credit:** Chris Ries
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-045/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Java. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the NEWT library due to the way that one of its classes uses reflection in its main method. When the class is used as the main-class in a JNLP file, this vulnerability can allow an attacker to call the main method of any trusted class with arbitrary arguments and with a trusted call stack, which in some cases can lead to execution of arbitrary code. The NEWT library can be installed without warnings because it is signed with a valid certificate recognized by the java install.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/javacpufeb2012-366318.html

## Disclosure Timeline

- 2011-11-26 - Vulnerability reported to vendor
- 2012-03-20 - Coordinated public release of advisory
