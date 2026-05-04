# ZDI-18-1082: Apple Safari Subframe Same-Origin Policy Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1082
- **ZDI-CAN:** ZDI-CAN-6416
- **Date:** 2018-09-24
- **CVE:** CVE-2018-4309
- **CVSS:** 6.4
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:N
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1082/
## Vulnerability Details

This vulnerability allows remote attackers to bypass the same-origin policy on vulnerable installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file and execute a user gesture within the rendered HTML. The specific flaw exists within the handling of subframes. The issue lies in the ability to execute arbitrary JavaScript without preserving the original origin. An attacker can leverage this vulnerability to execute script in the context of a different domain.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT209109

## Disclosure Timeline

- 2018-06-22 - Vulnerability reported to vendor
- 2018-09-24 - Coordinated public release of advisory
- 2018-09-24 - Advisory Updated
