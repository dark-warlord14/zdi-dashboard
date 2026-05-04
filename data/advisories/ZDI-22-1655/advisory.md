# ZDI-22-1655: (Pwn2Own) Microsoft Teams chat Client-Side Template Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1655
- **ZDI-CAN:** ZDI-CAN-17427
- **Date:** 2022-11-22
- **CVE:** N/A
- **CVSS:** 6.3
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Microsoft
- **Affected Products:** Teams
- **Credit:** Daniel Lim Wee Soong (@daniellimws), Li Jiantao (@CurseRed), Ngo Wei Lin (@Creastery), Poh Jia Hao (@Chocologicall) of STAR Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1655/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Teams. No user interaction is required if the attacker and target are in the same Teams organization. The specific flaw exists within the rendering of chat messages. Crafted data in a chat message can trigger execution of JavaScript composed from a user-supplied string. An attacker can leverage this vulnerability to execute code in the context of the current process at low integrity.

## Additional Details

Fixed on August 31, 2022 https://msrc.microsoft.com/update-guide/acknowledgement/online

## Disclosure Timeline

- 2022-05-25 - Vulnerability reported to vendor
- 2022-11-22 - Coordinated public release of advisory
