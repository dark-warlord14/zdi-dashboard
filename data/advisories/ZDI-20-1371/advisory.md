# ZDI-20-1371: Microsoft Windows DirectComposition Uninitialized Pointer Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1371
- **ZDI-CAN:** ZDI-CAN-11867
- **Date:** 2020-11-11
- **CVE:** CVE-2020-17057
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1371/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the implementation of DirectComposition in the Windows kernel. Crafted parameters to a system call can trigger access to a pointer prior to initialization. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the kernel.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-us/security-guidance/advisory/CVE-2020-17057

## Disclosure Timeline

- 2020-09-18 - Vulnerability reported to vendor
- 2020-11-11 - Coordinated public release of advisory
