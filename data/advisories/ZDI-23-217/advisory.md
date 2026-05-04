# ZDI-23-217: Parallels Desktop Updater Time-Of-Check Time-Of-Use Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-217
- **ZDI-CAN:** ZDI-CAN-18150
- **Date:** 2023-03-07
- **CVE:** CVE-2023-27323
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Parallels
- **Affected Products:** Desktop
- **Credit:** aegis
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-217/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Parallels Desktop. An attacker must first obtain the ability to execute low-privileged code on the target host system in order to exploit this vulnerability. The specific flaw exists within the Updater service. By creating a symbolic link, an attacker can abuse the service to execute a file. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of root.

## Additional Details

Parallels has issued an update to correct this vulnerability. More details can be found at: https://kb.parallels.com/125013

## Disclosure Timeline

- 2022-08-31 - Vulnerability reported to vendor
- 2023-03-07 - Coordinated public release of advisory
