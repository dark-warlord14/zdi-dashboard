# ZDI-26-248: NoMachine External Control of File Path Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-248
- **ZDI-CAN:** ZDI-CAN-28630
- **Date:** 2026-03-30
- **CVE:** CVE-2026-5054
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NoMachine
- **Affected Products:** NoMachine
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-248/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of NoMachine. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of command line parameters. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of root.

## Additional Details

Fixed in NoMachine version 9.4.14 https://kb.nomachine.com/SU03X00271

## Disclosure Timeline

- 2026-02-06 - Vulnerability reported to vendor
- 2026-03-30 - Coordinated public release of advisory
- 2026-03-30 - Advisory Updated
