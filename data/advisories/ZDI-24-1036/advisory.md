# ZDI-24-1036: Check Point ZoneAlarm Extreme Security Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1036
- **ZDI-CAN:** ZDI-CAN-21677
- **Date:** 2024-07-31
- **CVE:** CVE-2024-6233
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Check Point
- **Affected Products:** ZoneAlarm Extreme Security
- **Credit:** Filip Dragovic (@filip_dragovic)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1036/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Check Point ZoneAlarm Extreme Security. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Forensic Recorder service. By creating a symbolic link, an attacker can abuse the service to overwrite arbitrary files. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Fixed in version 4.2.712 https://www.zonealarm.com/software/extreme-security-nextgen

## Disclosure Timeline

- 2023-09-07 - Vulnerability reported to vendor
- 2024-07-31 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
