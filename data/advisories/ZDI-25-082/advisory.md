# ZDI-25-082: Parallels Desktop Technical Data Reporter Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-082
- **ZDI-CAN:** ZDI-CAN-25014
- **Date:** 2025-02-04
- **CVE:** CVE-2025-0413
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Parallels
- **Affected Products:** Desktop
- **Credit:** kn32
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-082/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Parallels Desktop. An attacker must first obtain the ability to execute low-privileged code on the target host system in order to exploit this vulnerability. The specific flaw exists within the Technical Data Reporter component. By creating a symbolic link, an attacker can abuse the service to change the permissions of arbitrary files. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of root.

## Additional Details

Fixed in: Parallels Client (Windows) v20.2-25889 Parallels RAS Core v19.4.3.2-25228 (Hotfix) Parallels Client (Windows) v19.4.3-25221 (Hotfix) Details can be found in https://kb.parallels.com/en/129018#section7 (version 19) and https://kb.parallels.com/en/130242 (version 20)

## Disclosure Timeline

- 2024-09-19 - Vulnerability reported to vendor
- 2025-02-04 - Coordinated public release of advisory
- 2025-06-25 - Advisory Updated
