# ZDI-23-712: Autodesk On-Demand Install Services Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-712
- **ZDI-CAN:** ZDI-CAN-19227
- **Date:** 2023-05-24
- **CVE:** CVE-2023-27908
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Autodesk
- **Affected Products:** On-Demand Install Services
- **Credit:** Filip Dragović
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-712/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Autodesk On-Demand Install Services. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the AdskAccessServiceHost service. By creating a symbolic link, an attacker can abuse the service to create a folder with a permissive DACL. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Autodesk has issued an update to correct this vulnerability. More details can be found at: https://www.autodesk.com/trust/security-advisories/adsk-sa-2023-0010

## Disclosure Timeline

- 2022-11-23 - Vulnerability reported to vendor
- 2023-05-24 - Coordinated public release of advisory
