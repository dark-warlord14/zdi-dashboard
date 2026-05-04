# ZDI-24-294: Microsoft Office Performance Monitor Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-294
- **ZDI-CAN:** ZDI-CAN-23146
- **Date:** 2024-03-13
- **CVE:** CVE-2024-26199
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Office
- **Credit:** Iván Almuiña from Hacking Corporation Sàrl
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-294/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Office. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Office Performance Monitor executable. By creating a symbolic link, an attacker can abuse the process to delete arbitrary files. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-26199

## Disclosure Timeline

- 2024-02-06 - Vulnerability reported to vendor
- 2024-03-13 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
