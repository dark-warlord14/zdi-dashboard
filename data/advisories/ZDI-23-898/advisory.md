# ZDI-23-898: (Pwn2Own) Canonical Ubuntu tcindex Double-Free Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-898
- **ZDI-CAN:** ZDI-CAN-20667
- **Date:** 2023-07-06
- **CVE:** CVE-2023-1829
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Canonical
- **Affected Products:** Ubuntu
- **Credit:** Kyle Zeng from ASU SEFCOM
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-898/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Canonical Ubuntu. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the tcindex module. The issue results from the lack of validating the existence of an object prior to performing further free operations on the object. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the kernel.

## Additional Details

Canonical has issued an update to correct this vulnerability. More details can be found at: https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=8c710f75256bb3cf05ac7b1672c82b92c43f3d28

## Disclosure Timeline

- 2023-05-09 - Vulnerability reported to vendor
- 2023-07-06 - Coordinated public release of advisory
