# ZDI-15-108: (Pwn2Own) Mozilla Firefox SVG DOMAttrModified Same-Origin Policy Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-108
- **ZDI-CAN:** ZDI-CAN-2825
- **Date:** 2015-04-03
- **CVE:** CVE-2015-0818
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Mozilla
- **Affected Products:** Firefox
- **Credit:** Mariusz Mlynski
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-108/
## Vulnerability Details

This vulnerability allows remote attackers to bypass the same-origin policy on vulnerable installations of Mozilla Firefox. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of SVG format content navigation. By using a DOMAttrModified mutation event listener, an attacker can inject an arbitrary URL into the history, and cause Firefox to break the same-origin isolation policy.

## Additional Details

Mozilla has issued an update to correct this vulnerability. More details can be found at: https://bugzilla.mozilla.org/show_bug.cgi?id=1144988

## Disclosure Timeline

- 2015-03-18 - Vulnerability reported to vendor
- 2015-04-03 - Coordinated public release of advisory
