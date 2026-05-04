# ZDI-20-1254: Microsoft Windows Group Policy Client Service Link Resolution Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1254
- **ZDI-CAN:** ZDI-CAN-11622
- **Date:** 2020-10-19
- **CVE:** CVE-2020-16939
- **CVSS:** 7.3
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Nabeel Ahmed (@rogue_kdc) of NTT
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1254/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Group Policy Client service. By creating a junction, an attacker can abuse the service to gain control of files and folders. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of an administrator.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-us/security-guidance/advisory/CVE-2020-16939

## Disclosure Timeline

- 2020-08-05 - Vulnerability reported to vendor
- 2020-10-19 - Coordinated public release of advisory
