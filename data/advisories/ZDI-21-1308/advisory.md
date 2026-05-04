# ZDI-21-1308: Microsoft Windows Installer Service Link Following Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1308
- **ZDI-CAN:** ZDI-CAN-14616
- **Date:** 2021-11-11
- **CVE:** CVE-2021-41379
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Abdelhamid Naceri
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1308/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Windows Installer service. By creating a junction, an attacker can abuse the service to delete a file or directory. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-41379

## Disclosure Timeline

- 2021-08-10 - Vulnerability reported to vendor
- 2021-11-11 - Coordinated public release of advisory
