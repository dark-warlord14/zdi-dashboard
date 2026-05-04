# ZDI-22-943: Parallels Desktop Updater Race Condition Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-943
- **ZDI-CAN:** ZDI-CAN-16396
- **Date:** 2022-06-30
- **CVE:** CVE-2022-34892
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Parallels
- **Affected Products:** Desktop
- **Credit:** aegis
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-943/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Parallels Desktop. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the update machanism. The issue results from the lack of proper locking when performing operations on an object. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of root.

## Additional Details

Parallels has issued an update to correct this vulnerability. More details can be found at: https://kb.parallels.com/125013

## Disclosure Timeline

- 2022-03-09 - Vulnerability reported to vendor
- 2022-06-30 - Coordinated public release of advisory
