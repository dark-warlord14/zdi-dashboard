# ZDI-15-009: (Mobile Pwn2Own) Apple Safari Set Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-009
- **ZDI-CAN:** ZDI-CAN-2611
- **Date:** 2015-01-27
- **CVE:** CVE-2014-4477
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** lokihardt@ASRT
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-009/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of Set objects. The issue lies in the usage of an iterator after clearing the object. An attacker can leverage this vulnerability to execute code under the context of the renderer process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/en-us/HT204243

## Disclosure Timeline

- 2014-11-13 - Vulnerability reported to vendor
- 2015-01-27 - Coordinated public release of advisory
