# ZDI-24-523: Phoenix Contact CHARX SEC-3100 Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-523
- **ZDI-CAN:** ZDI-CAN-20923
- **Date:** 2024-05-29
- **CVE:** CVE-2024-28137
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Phoenix Contact
- **Affected Products:** CHARX SEC-3100
- **Credit:** Todd Manning
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-523/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Phoenix Contact CHARX SEC-3100 charging controllers. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the /etc/init.d/user-applications script. By creating a symbolic link, an attacker can abuse the script to change ownership of arbitrary files. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of root.

## Additional Details

Phoenix Contact has issued an update to correct this vulnerability. More details can be found at: https://cert.vde.com/en/advisories/VDE-2024-019/

## Disclosure Timeline

- 2024-02-21 - Vulnerability reported to vendor
- 2024-05-29 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
