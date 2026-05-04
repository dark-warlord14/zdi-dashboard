# ZDI-21-422: (Pwn2Own) Canonical Ubuntu ShiftFS File System Double Free Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-422
- **ZDI-CAN:** ZDI-CAN-13562
- **Date:** 2021-04-21
- **CVE:** CVE-2021-3492
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Canonical
- **Affected Products:** Ubuntu
- **Credit:** Vincent Dehors (@vdehors) from Synacktiv (@Synacktiv)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-422/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Canonical Ubuntu. An attacker must first obtain the ability to execute high-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the ShiftFS module. The issue results from the lack of validating the existence of an object prior to performing further free operations on the object. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the kernel.

## Additional Details

Canonical has issued an update to correct this vulnerability. More details can be found at: https://ubuntu.com/security/CVE-2021-3492

## Disclosure Timeline

- 2021-04-19 - Vulnerability reported to vendor
- 2021-04-21 - Coordinated public release of advisory
