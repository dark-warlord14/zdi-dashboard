# ZDI-22-1406: Tesla wowlan_config Use-After-Free Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1406
- **ZDI-CAN:** ZDI-CAN-17543
- **Date:** 2022-10-07
- **CVE:** CVE-2022-42430
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Tesla
- **Affected Products:** Model 3
- **Credit:** Vincent DEHORS of @Synacktiv
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1406/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected Tesla vehicles. An attacker must first obtain the ability to execute privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of the wowlan_config data structure. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of root.

## Additional Details

Fixed in Tesla’s 2022.28 release.

## Disclosure Timeline

- 2022-05-24 - Vulnerability reported to vendor
- 2022-10-07 - Coordinated public release of advisory
