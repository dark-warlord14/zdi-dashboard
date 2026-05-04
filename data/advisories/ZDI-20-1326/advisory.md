# ZDI-20-1326: Micro Focus Operations Bridge Manager Service Incorrect Permission Assignment Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1326
- **ZDI-CAN:** ZDI-CAN-11204
- **Date:** 2020-10-28
- **CVE:** CVE-2020-11858
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Micro Focus
- **Affected Products:** Operations Bridge Manager
- **Credit:** Pedro Ribeiro (pedrib@gmail.com | @pedrib1337) from Agile Information Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1326/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Micro Focus Operations Bridge Manager. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the product installer. The issue results from incorrect permissions set on the installation directory. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of SYSTEM.

## Additional Details

Micro Focus has issued an update to correct this vulnerability. More details can be found at: https://softwaresupport.softwaregrp.com/doc/KM03747658

## Disclosure Timeline

- 2020-07-02 - Vulnerability reported to vendor
- 2020-10-28 - Coordinated public release of advisory
