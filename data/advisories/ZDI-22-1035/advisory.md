# ZDI-22-1035: Autodesk Desktop App Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1035
- **ZDI-CAN:** ZDI-CAN-16887
- **Date:** 2022-07-29
- **CVE:** CVE-2022-33882
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Autodesk
- **Affected Products:** Desktop App
- **Credit:** Michael DePlante (@izobashi) of Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1035/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Autodesk Desktop App. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of updates. By creating a symbolic link, an attacker can abuse the application to delete a file. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Autodesk has issued an update to correct this vulnerability. More details can be found at: https://www.autodesk.com/trust/security-advisories/adsk-sa-2022-0015

## Disclosure Timeline

- 2022-03-16 - Vulnerability reported to vendor
- 2022-07-29 - Coordinated public release of advisory
