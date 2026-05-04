# ZDI-23-220: Parallels Desktop Toolgate XML Injection Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-220
- **ZDI-CAN:** ZDI-CAN-19187
- **Date:** 2023-03-07
- **CVE:** CVE-2023-27328
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Parallels
- **Affected Products:** Desktop
- **Credit:** kn32
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-220/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Parallels Desktop. An attacker must first obtain the ability to execute low-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the Toolgate component. The issue results from the lack of proper validation of a user-supplied string before using it to construct an XML document. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the hypervisor.

## Additional Details

Parallels has issued an update to correct this vulnerability. More details can be found at: https://kb.parallels.com/125013

## Disclosure Timeline

- 2022-11-03 - Vulnerability reported to vendor
- 2023-03-07 - Coordinated public release of advisory
