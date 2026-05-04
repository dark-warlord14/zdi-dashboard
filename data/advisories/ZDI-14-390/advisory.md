# ZDI-14-390: (Pwn2Own) Apple OS X WindowsServer Sandbox Escape Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-390
- **ZDI-CAN:** ZDI-CAN-2222
- **Date:** 2014-12-02
- **CVE:** CVE-2014-1314
- **CVSS:** 4.6
- **CVSS Vector:** AV:L/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** OS X
- **Credit:** Liang Chen of KeenTeam
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-390/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple OS X. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within WindowServer. The issue lies in the failure to prevent sandboxed applications from creating new sessions. An attacker can leverage this to execute code outside the context of the sandbox.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/en-us/HT202966

## Disclosure Timeline

- 2014-03-13 - Vulnerability reported to vendor
- 2014-12-02 - Coordinated public release of advisory
