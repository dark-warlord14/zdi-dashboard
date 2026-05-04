# ZDI-11-182: Oracle Java IE Browser Plugin Corrupted Window Procedure Hook Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-182
- **ZDI-CAN:** ZDI-CAN-1046
- **Date:** 2011-06-08
- **CVE:** CVE-2011-0817
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** Java Runtime
- **Credit:** Stephen Fewer of Harmony Security (www.harmonysecurity.com)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-182/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of the Oracle Sun Java Runtime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the JP2IEXP.dll browser plugin. The module creates a window hook when an applet is instantiated within the context of a browser. If the underlying DOM element is cloned and the parent object removed, a dangling reference can exist. When the module attempts to walk the relationship list to call the window hook, the process can be made to jump into uninitialized heap memory. This can be exploited by an attacker to execute code under the context of the user running the browser.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/javacpujune2011-313339.html

## Disclosure Timeline

- 2011-01-21 - Vulnerability reported to vendor
- 2011-06-08 - Coordinated public release of advisory
