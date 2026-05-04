# ZDI-21-606: (Pwn2Own) Canonical Ubuntu eBPF Out-Of-Bounds Access Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-606
- **ZDI-CAN:** ZDI-CAN-13590
- **Date:** 2021-05-25
- **CVE:** CVE-2021-3490
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Canonical
- **Affected Products:** Ubuntu
- **Credit:** Manfred Paul (@_manfp) of the RedRocket CTF team (@redrocket_ctf)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-606/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Canonical Ubuntu. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of eBPF programs. The issue results from the lack of proper validation of user-supplied eBPF programs prior to executing them. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the kernel.

## Additional Details

Canonical has issued an update to correct this vulnerability. More details can be found at: https://www.openwall.com/lists/oss-security/2021/05/11/11

## Disclosure Timeline

- 2021-05-14 - Vulnerability reported to vendor
- 2021-05-25 - Coordinated public release of advisory
