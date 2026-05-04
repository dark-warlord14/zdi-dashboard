# ZDI-14-091: (Pwn2Own) Apple Safari Heap Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-091
- **ZDI-CAN:** ZDI-CAN-2221
- **Date:** 2014-04-11
- **CVE:** CVE-2014-1303
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** Liang Chen of KeenTeam
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-091/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of CSS rules. The issue lies in the improper handling of CSSSelector elements. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT6181

## Disclosure Timeline

- 2014-03-13 - Vulnerability reported to vendor
- 2014-04-11 - Coordinated public release of advisory
