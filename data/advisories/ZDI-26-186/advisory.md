# ZDI-26-186: Fortinet FortiClient Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-186
- **ZDI-CAN:** ZDI-CAN-27581
- **Date:** 2026-03-10
- **CVE:** CVE-2026-24018
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Fortinet
- **Affected Products:** FortiClient
- **Credit:** Febin Mon Saji from Astra Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-186/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Fortinet FortiClient. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of certain shared objects. By creating a symbolic link, an attacker can abuse the service to load and execute arbitrary shared objects. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of root.

## Additional Details

Fortinet has issued an update to correct this vulnerability. More details can be found at: https://www.fortiguard.com/psirt/FG-IR-26-083

## Disclosure Timeline

- 2025-10-29 - Vulnerability reported to vendor
- 2026-03-10 - Coordinated public release of advisory
- 2026-03-10 - Advisory Updated
