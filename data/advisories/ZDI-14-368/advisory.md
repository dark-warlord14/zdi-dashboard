# ZDI-14-368: Apple OS X GateKeeper Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-368
- **ZDI-CAN:** ZDI-CAN-1923
- **Date:** 2014-10-24
- **CVE:** CVE-2014-4391
- **CVSS:** 5.6
- **CVSS Vector:** AV:L/AC:L/Au:N/C:P/I:C/A:N
- **Affected Vendors:** Apple
- **Affected Products:** OS X
- **Credit:** Christopher Hickstein
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-368/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple OS X. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within Gatekeeper. The issue lies in the usage of signed applications that do not sign the frameworks they depend on. An attacker can leverage this vulnerability to execute code under the context of the user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT6535

## Disclosure Timeline

- 2013-07-30 - Vulnerability reported to vendor
- 2014-10-24 - Coordinated public release of advisory
