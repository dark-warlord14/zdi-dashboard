# ZDI-21-590: (Pwn2Own) Canonical Ubuntu eBPF Out-Of-Bounds Access Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-590
- **ZDI-CAN:** ZDI-CAN-13586
- **Date:** 2021-05-14
- **CVE:** CVE-2021-3489
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Canonical
- **Affected Products:** Ubuntu
- **Credit:** Ryota Shiga(@Ga_ryo_) of Flatt:w Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-590/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Canonical Ubuntu. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of eBPF programs. The issue results from the lack of proper validation of user-supplied eBPF programs prior to executing them. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the kernel.

## Additional Details

Canonical has issued an update to correct this vulnerability. More details can be found at: https://www.openwall.com/lists/oss-security/2021/05/11/10

## Disclosure Timeline

- 2021-04-22 - Vulnerability reported to vendor
- 2021-05-14 - Coordinated public release of advisory
