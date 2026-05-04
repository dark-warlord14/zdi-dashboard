# ZDI-22-049: Microsoft Windows SilentCleanup Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-049
- **ZDI-CAN:** ZDI-CAN-14660
- **Date:** 2022-01-13
- **CVE:** CVE-2022-21838
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Abdelhamid Naceri
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-049/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the SilentCleanup scheduled task. By creating a symbolic link, an attacker can abuse the task to delete a folder. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-21838

## Disclosure Timeline

- 2021-09-03 - Vulnerability reported to vendor
- 2022-01-13 - Coordinated public release of advisory
