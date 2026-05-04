# ZDI-12-037: Oracle Java Web Start JNLP Double Quote Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-037
- **ZDI-CAN:** ZDI-CAN-1407
- **Date:** 2012-02-22
- **CVE:** N/A
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Oracle
- **Affected Products:** Java Runtime
- **Credit:** Chris Ries
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-037/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Java Webstart. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within javaws.exe . Java Web Start does not safely handle double quotes that are placed anywhere except the beginning of certain property names in JNLP files. As a result, double quotes can be used to inject arbitrary command-line arguments into a javaw.exe process. Leveraging this would allow a remote attacker to execute code under the context of the user.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/javacpufeb2012-366318.html

## Disclosure Timeline

- 2011-10-28 - Vulnerability reported to vendor
- 2012-02-22 - Coordinated public release of advisory
