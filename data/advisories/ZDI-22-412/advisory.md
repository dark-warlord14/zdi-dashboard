# ZDI-22-412: (Pwn2Own) Cisco RV340 confd_cli Unnecessary Privileges Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-412
- **ZDI-CAN:** ZDI-CAN-15886
- **Date:** 2022-02-22
- **CVE:** CVE-2022-20701
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Cisco
- **Affected Products:** RV340
- **Credit:** Benjamin Grap, Hanno Heinrichs and Lukas Kupczyk of CrowdStrike Intelligence
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-412/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Cisco RV340 routers. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within confd_cli. The issue results from executing user commands at an unnecessarily high privilege level. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of root.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-smb-mult-vuln-KA9PK6D

## Disclosure Timeline

- 2022-01-26 - Vulnerability reported to vendor
- 2022-02-22 - Coordinated public release of advisory
