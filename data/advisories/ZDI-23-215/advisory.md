# ZDI-23-215: Parallels Desktop Toolgate Time-Of-Check Time-Of-Use Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-215
- **ZDI-CAN:** ZDI-CAN-18964
- **Date:** 2023-03-07
- **CVE:** CVE-2023-27327
- **CVSS:** 7.5
- **CVSS Vector:** AV:L/AC:H/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Parallels
- **Affected Products:** Desktop
- **Credit:** kn32
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-215/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Parallels Desktop. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the Toolgate component. The issue results from the lack of proper locking when performing operations on an object. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the current user on the host system.

## Additional Details

Parallels has issued an update to correct this vulnerability. More details can be found at: https://kb.parallels.com/125013

## Disclosure Timeline

- 2022-11-03 - Vulnerability reported to vendor
- 2023-03-07 - Coordinated public release of advisory
