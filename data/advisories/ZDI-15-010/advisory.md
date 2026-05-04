# ZDI-15-010: (Mobile Pwn2Own) Apple iOS SSL Sandbox Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-010
- **ZDI-CAN:** ZDI-CAN-2612
- **Date:** 2015-01-27
- **CVE:** CVE-2014-8840
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** iOS
- **Credit:** lokihardt@ASRT
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-010/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on vulnerable installations of Apple iOS. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of SSL connections. The issue lies in the implicit trust of sites that offer URL redirection services. An attacker can leverage this vulnerability to execute code outside the context of the sandbox.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/en-us/HT204245

## Disclosure Timeline

- 2014-11-13 - Vulnerability reported to vendor
- 2015-01-27 - Coordinated public release of advisory
