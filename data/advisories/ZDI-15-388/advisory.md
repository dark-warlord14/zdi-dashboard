# ZDI-15-388: (Pwn2Own) Microsoft Windows TrueType Fonts Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-388
- **ZDI-CAN:** ZDI-CAN-2818
- **Date:** 2015-08-11
- **CVE:** CVE-2015-2455
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** KeenTeam's Jihui Lu and Peter Hlavaty
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-388/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of the IUP instruction (opcode 0x31) in TrueType fonts. A crafted font can cause point patching to modify arbitrary addresses in the Windows kernel. This can be leveraged by an attacker to run arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS15-080

## Disclosure Timeline

- 2015-03-18 - Vulnerability reported to vendor
- 2015-08-11 - Coordinated public release of advisory
