# ZDI-22-420: (Pwn2Own) Cisco RV340 utility-ping-request Insecure Temporary File Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-420
- **ZDI-CAN:** ZDI-CAN-15946
- **Date:** 2022-02-22
- **CVE:** CVE-2022-20702
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Cisco
- **Affected Products:** RV340
- **Credit:** Jeongun Baek of Diffense
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-420/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Cisco RV340 routers. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the utility-ping-request script. The issue results from the creation of a temporary file with insecure permissions. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of root.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-smb-mult-vuln-KA9PK6D

## Disclosure Timeline

- 2021-12-10 - Vulnerability reported to vendor
- 2022-02-22 - Coordinated public release of advisory
