# ZDI-24-496: NETGEAR ProSAFE Network Management System Default Credentials Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-496
- **ZDI-CAN:** ZDI-CAN-22755
- **Date:** 2024-05-22
- **CVE:** CVE-2024-5245
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NETGEAR
- **Affected Products:** ProSAFE Network Management System
- **Credit:** 191bb9f9c7b3a89d5a586e15299e24417a4aca4d
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-496/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of NETGEAR ProSAFE Network Management System. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the product installer. The issue results from the use of default MySQL credentials. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000066164/Security-Advisory-for-Multiple-Vulnerabilities-on-the-NMS300-PSV-2024-0003-PSV-2024-0004

## Disclosure Timeline

- 2024-01-11 - Vulnerability reported to vendor
- 2024-05-22 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
