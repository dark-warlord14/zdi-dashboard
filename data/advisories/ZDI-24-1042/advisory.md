# ZDI-24-1042: NoMachine Uncontrolled Search Path Element Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1042
- **ZDI-CAN:** ZDI-CAN-24039
- **Date:** 2024-08-01
- **CVE:** CVE-2024-7253
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NoMachine
- **Affected Products:** NoMachine
- **Credit:** bananabr
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1042/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of NoMachine. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within nxnode.exe. The process loads a library from an unsecured location. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

NoMachine has issued an update to correct this vulnerability. More details can be found at: https://kb.nomachine.com/TR07V11184

## Disclosure Timeline

- 2024-07-16 - Vulnerability reported to vendor
- 2024-08-01 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
