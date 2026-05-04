# ZDI-21-1104: McAfee Endpoint Security Incorrect Permission Assignment Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1104
- **ZDI-CAN:** ZDI-CAN-13800
- **Date:** 2021-09-22
- **CVE:** CVE-2021-31847
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** McAfee
- **Affected Products:** Endpoint Security
- **Credit:** @Kharosx0
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1104/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of McAfee Endpoint Security. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the installer. The issue results from incorrect permissions set on a resource used by the installer. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

McAfee has issued an update to correct this vulnerability. More details can be found at: https://kc.mcafee.com/corporate/index?page=content&id=SB10369

## Disclosure Timeline

- 2021-06-16 - Vulnerability reported to vendor
- 2021-09-22 - Coordinated public release of advisory
