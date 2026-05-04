# ZDI-17-476: (Pwn2Own) Microsoft Windows CLFS Driver Uninitialized Memory Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-476
- **ZDI-CAN:** ZDI-CAN-4577
- **Date:** 2017-07-11
- **CVE:** CVE-2017-8590
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** pgboy and zhong_sf of Qihoo 360Vulcan Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-476/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Common Log File System (CLFS) driver. A crafted call to this driver can trigger access to memory prior to initialization. An attacker can leverage this vulnerability to escalate privilege to the level of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2017-8590

## Disclosure Timeline

- 2017-03-16 - Vulnerability reported to vendor
- 2017-07-11 - Coordinated public release of advisory
