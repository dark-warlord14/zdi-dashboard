# ZDI-25-076: NoMachine Incorrect Permission Assignment Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-076
- **ZDI-CAN:** ZDI-CAN-25094
- **Date:** 2025-02-03
- **CVE:** CVE-2024-9632
- **CVSS:** 6.7
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** NoMachine
- **Affected Products:** NoMachine
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-076/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of NoMachine. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the product installer. The issue results from incorrect permissions on a folder. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

NoMachine has issued an update to correct this vulnerability. More details can be found at: https://kb.nomachine.com/SU01W00263

## Disclosure Timeline

- 2024-09-26 - Vulnerability reported to vendor
- 2025-02-03 - Coordinated public release of advisory
- 2025-02-03 - Advisory Updated
