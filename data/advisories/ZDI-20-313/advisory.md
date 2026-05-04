# ZDI-20-313: Microsoft Windows AppX Deployment Service Hard Link Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-313
- **ZDI-CAN:** ZDI-CAN-10131
- **Date:** 2020-03-18
- **CVE:** N/A
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Nabeel Ahmed (@rogue_kdc) of NTT
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-313/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the AppX Deployment Service. By creating a hard link, an attacker can abuse the service to overwrite the contents of a chosen file. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-us/security-guidance/acknowledgments

## Disclosure Timeline

- 2020-02-26 - Vulnerability reported to vendor
- 2020-03-18 - Coordinated public release of advisory
