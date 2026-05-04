# ZDI-15-258: (Pwn2Own) Apple OS X XSS Sandbox Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-258
- **ZDI-CAN:** ZDI-CAN-2837
- **Date:** 2015-06-24
- **CVE:** N/A
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** OS X
- **Credit:** lokihardt@ASRT
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-258/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple OS X. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within certain URLs in the protocol handler whitelist. The issue lies in the ability to inject JavaScript within the 'entity' parameter. An attacker can leverage this vulnerability to execute code outside the context of the sandbox.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT201536 no CVE, server-side fix

## Disclosure Timeline

- 2015-03-19 - Vulnerability reported to vendor
- 2015-06-24 - Coordinated public release of advisory
