# ZDI-26-115: Fortinet FortiClient VPN FCConfig Utility Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-115
- **ZDI-CAN:** ZDI-CAN-25710
- **Date:** 2026-02-19
- **CVE:** CVE-2025-62676
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Fortinet
- **Affected Products:** FortiClient VPN
- **Credit:** Alexander Staalgaard
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-115/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Fortinet FortiClient VPN. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the FortiClient Configuration Daemon. By creating a junction, an attacker can abuse the service to overwrite arbitrary files. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Fortinet has issued an update to correct this vulnerability. More details can be found at: https://fortiguard.fortinet.com/psirt/FG-IR-25-661

## Disclosure Timeline

- 2025-05-29 - Vulnerability reported to vendor
- 2026-02-19 - Coordinated public release of advisory
- 2026-02-19 - Advisory Updated
