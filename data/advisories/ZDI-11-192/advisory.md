# ZDI-11-192: Oracle Java Web Start Command Argument Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-192
- **ZDI-CAN:** ZDI-CAN-1098
- **Date:** 2011-06-08
- **CVE:** CVE-2011-0863
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** Java Runtime
- **Credit:** Chris Ries
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-192/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Java. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the way Java webstart parses certain properties from the jnlp file. Due to insufficient quote escaping it is possible to supply additional command line parameters to the java process. By crafting such parameters, an attacker can execute remote code under the context of the user running the process.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/javacpujune2011-313339.html

## Disclosure Timeline

- 2011-01-21 - Vulnerability reported to vendor
- 2011-06-08 - Coordinated public release of advisory
