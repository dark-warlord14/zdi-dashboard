# ZDI-22-499: Microsoft Windows CD-ROM Driver Uninitialized Pointer Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-499
- **ZDI-CAN:** ZDI-CAN-7819
- **Date:** 2022-03-09
- **CVE:** CVE-2022-24455
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Hugo Cao of SandCastle, LilangWu, Moony Li of mobile security research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-499/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the CD-ROM driver. Crafted data sent to IOCTL 0x0056c064 can trigger access to a pointer prior to initialization. An attacker can leverage this vulnerability to escalate privileges to the level of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-24455

## Disclosure Timeline

- 2019-01-23 - Vulnerability reported to vendor
- 2022-03-09 - Coordinated public release of advisory
