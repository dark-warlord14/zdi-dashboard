# ZDI-24-802: (0Day) Poly Plantronics Hub Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-802
- **ZDI-CAN:** ZDI-CAN-18271
- **Date:** 2024-06-18
- **CVE:** CVE-2024-6147
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Poly
- **Affected Products:** Plantronics Hub
- **Credit:** Michael DePlante (@izobashi) of Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-802/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Poly Plantronics Hub. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Spokes Update Service. By creating a symbolic link, an attacker can abuse the service to delete a file. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Poly has issued an update to correct this vulnerability. More details can be found at: https://support.hp.com/us-en/document/ish_9869257-9869285-16/hpsbpy03895

## Disclosure Timeline

- 2022-08-10 - Vulnerability reported to vendor
- 2024-06-18 - Coordinated public release of advisory
- 2024-08-30 - Advisory Updated
