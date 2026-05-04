# ZDI-25-1050: Microsoft Azure Virtual Desktop Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1050
- **ZDI-CAN:** ZDI-CAN-26573
- **Date:** 2025-12-09
- **CVE:** N/A
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Azure Virtual Desktop
- **Credit:** Filip Dragovic (@filip_dragovic)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1050/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Azure Virtual Desktop. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the RdAgent service. By creating a junction, an attacker can abuse the service to delete arbitrary folders and files. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-us/security-guidance/researcher-acknowledgments-online-services

## Disclosure Timeline

- 2025-08-01 - Vulnerability reported to vendor
- 2025-12-09 - Coordinated public release of advisory
- 2025-12-09 - Advisory Updated
