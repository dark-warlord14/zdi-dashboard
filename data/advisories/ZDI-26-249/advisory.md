# ZDI-26-249: NoMachine Uncontrolled Search Path Element Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-249
- **ZDI-CAN:** ZDI-CAN-28494
- **Date:** 2026-03-30
- **CVE:** CVE-2026-5055
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NoMachine
- **Affected Products:** NoMachine
- **Credit:** khongtrang
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-249/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of NoMachine. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the NoMachine Device Server. The product loads a library from an unsecured location. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Fixed in NoMachine version 9.4.14 https://kb.nomachine.com/SU03X00271

## Disclosure Timeline

- 2025-12-24 - Vulnerability reported to vendor
- 2026-03-30 - Coordinated public release of advisory
- 2026-03-30 - Advisory Updated
