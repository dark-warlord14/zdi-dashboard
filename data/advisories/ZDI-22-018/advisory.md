# ZDI-22-018: Microsoft Windows Update Assistant Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-018
- **ZDI-CAN:** ZDI-CAN-14770
- **Date:** 2022-01-06
- **CVE:** CVE-2021-43237
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Abdelhamid Naceri
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-018/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. Additional user interaction is required in that an administrator must begin a version update of Windows. The specific flaw exists within Windows Update Assistant. By creating a directory junction, an attacker can abuse Windows Update Assistant to change the DACL on an arbitrary file. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-43237

## Disclosure Timeline

- 2021-09-03 - Vulnerability reported to vendor
- 2022-01-06 - Coordinated public release of advisory
