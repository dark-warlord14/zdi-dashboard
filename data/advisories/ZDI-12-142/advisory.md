# ZDI-12-142: Oracle Java WebStart Browser Argument Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-142
- **ZDI-CAN:** ZDI-CAN-1502
- **Date:** 2012-08-17
- **CVE:** CVE-2012-1713
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** Java Runtime
- **Credit:** Chris Ries
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-142/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Java. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the BasicService.showDocument Java Webstart function. This function allows additional parameters to be passed to the browser. Depending on which browser the user has set as default browser this could lead to remote code execution under the context of the current user.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/javacpujun2012-1515912.html

## Disclosure Timeline

- 2012-03-14 - Vulnerability reported to vendor
- 2012-08-17 - Coordinated public release of advisory
