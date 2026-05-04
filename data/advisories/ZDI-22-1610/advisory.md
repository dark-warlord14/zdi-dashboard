# ZDI-22-1610: (Pwn2Own) Microsoft Teams electronSafeIpc Arbitrary File Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1610
- **ZDI-CAN:** ZDI-CAN-17466
- **Date:** 2022-11-21
- **CVE:** N/A
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Teams
- **Credit:** Daniel Lim Wee Soong (@daniellimws), Li Jiantao (@CurseRed), Ngo Wei Lin (@Creastery), Poh Jia Hao (@Chocologicall) of STAR Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1610/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Teams. No user interaction is required if the attacker and target are in the same Teams organization. The specific flaw exists within the communication API. The issue lies in the handling of the electronSafeIpc variable, which allows an arbitrary file write with attacker-controlled data. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fixed on August 31, 2022 https://msrc.microsoft.com/update-guide/acknowledgement/online

## Disclosure Timeline

- 2022-05-25 - Vulnerability reported to vendor
- 2022-11-21 - Coordinated public release of advisory
