# ZDI-11-086: Oracle Java Webstart Trusted JNLP Extension Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-086
- **ZDI-CAN:** ZDI-CAN-976
- **Date:** 2011-02-15
- **CVE:** CVE-2010-4463
- **CVSS:** 9.7
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:P
- **Affected Vendors:** Oracle
- **Affected Products:** Java Runtime
- **Credit:** Peter Csepely
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-086/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle's Java Runtime Environment. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the Java Webstart loader of the Java Runtime Environment. When parsing a .jnlp file containing an extension, the loader will honor the permissions defined within. This will allow one to explicitly define the security permissions of their java component which will then get executed. This will allow one to execute code outside of the context of the JRE sandbox.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/javacpufeb2011-304611.html

## Disclosure Timeline

- 2010-10-18 - Vulnerability reported to vendor
- 2011-02-15 - Coordinated public release of advisory
