# ZDI-11-083: Oracle Java Applet Clipboard Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-083
- **ZDI-CAN:** ZDI-CAN-628
- **Date:** 2011-02-15
- **CVE:** CVE-2010-4465
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** Java Runtime
- **Credit:** Sami Koivu
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-083/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of the Oracle Java Runtime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw is due to insufficient defenses against system clipboard hijacking. When in focus, a handle to the system clipboard can be retrieved without user interaction by a malicious component. The clipboard can then be arbitrarily read from or written to. By writing a TransferableProxy object to the system clipboard and then forcing a paste action, arbitrary code can be executed under the context of the user invoking the JRE.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/javacpufeb2011-304611.html

## Disclosure Timeline

- 2010-01-26 - Vulnerability reported to vendor
- 2011-02-15 - Coordinated public release of advisory
