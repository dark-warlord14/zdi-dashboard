# ZDI-20-1217: Micro Focus Operations Bridge Reporter HPE-OBR Incorrect Permission Assignment Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1217
- **ZDI-CAN:** ZDI-CAN-11073
- **Date:** 2020-09-23
- **CVE:** CVE-2020-11855
- **CVSS:** 8.4
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Micro Focus
- **Affected Products:** Operations Bridge Reporter
- **Credit:** Pedro Ribeiro (pedrib@gmail.com|@pedrib1337) from Agile Information Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1217/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Micro Focus Operations Bridge Reporter. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the product's installer. The issue results from incorrect permissions set on a resource used by the service. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of SYSTEM.

## Additional Details

Micro Focus has issued an update to correct this vulnerability. More details can be found at: https://softwaresupport.softwaregrp.com/doc/KM03710590

## Disclosure Timeline

- 2020-05-27 - Vulnerability reported to vendor
- 2020-09-23 - Coordinated public release of advisory
