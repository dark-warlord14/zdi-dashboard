# ZDI-21-328: Microsoft Windows Setup Directory Junction Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-328
- **ZDI-CAN:** ZDI-CAN-12109
- **Date:** 2021-03-17
- **CVE:** CVE-2021-26889
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Abdelhamid Naceri (halov)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-328/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within Windows Setup. By creating a directory junction, an attacker can abuse Windows Setup to create a file in an arbitrary location. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-26889

## Disclosure Timeline

- 2020-11-11 - Vulnerability reported to vendor
- 2021-03-17 - Coordinated public release of advisory
