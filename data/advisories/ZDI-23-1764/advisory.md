# ZDI-23-1764: Check Point ZoneAlarm Extreme Security Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1764
- **ZDI-CAN:** ZDI-CAN-19062
- **Date:** 2023-12-12
- **CVE:** CVE-2023-28134
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Check Point
- **Affected Products:** ZoneAlarm Extreme Security
- **Credit:** Filip Dragovic
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1764/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Check Point ZoneAlarm Extreme Security. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Remediation Service. By creating a symbolic link, an attacker can abuse the service to change the DACL on a folder. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Check Point has issued an update to correct this vulnerability. More details can be found at: https://support.checkpoint.com/results/sk/sk181597

## Disclosure Timeline

- 2022-11-21 - Vulnerability reported to vendor
- 2023-12-12 - Coordinated public release of advisory
