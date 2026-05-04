# ZDI-22-716: Zoom Client Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-716
- **ZDI-CAN:** ZDI-CAN-16162
- **Date:** 2022-05-09
- **CVE:** CVE-2022-22782
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Zoom
- **Affected Products:** Client
- **Credit:** @Kharosx0
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-716/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Zoom Client. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the installer. By creating a symbolic link, an attacker can abuse the installer to delete a directory. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Zoom has issued an update to correct this vulnerability. More details can be found at: https://explore.zoom.us/en/trust/security/security-bulletin/

## Disclosure Timeline

- 2022-01-07 - Vulnerability reported to vendor
- 2022-05-09 - Coordinated public release of advisory
