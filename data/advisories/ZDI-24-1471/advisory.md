# ZDI-24-1471: Panda Security Dome PSANHost Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1471
- **ZDI-CAN:** ZDI-CAN-23479
- **Date:** 2024-11-11
- **CVE:** CVE-2024-8424
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Panda Security
- **Affected Products:** Dome
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1471/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Panda Security Dome. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Application Host Service. By creating a symbolic link, an attacker can abuse the service to delete a file. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Panda Security has issued an update to correct this vulnerability. More details can be found at: https://www.watchguard.com/wgrd-psirt/advisory/wgsa-2024-00017

## Disclosure Timeline

- 2024-04-17 - Vulnerability reported to vendor
- 2024-11-11 - Coordinated public release of advisory
- 2024-11-11 - Advisory Updated
