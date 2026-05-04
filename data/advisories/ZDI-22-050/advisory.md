# ZDI-22-050: Microsoft Windows User Profile Service Directory Junction Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-050
- **ZDI-CAN:** ZDI-CAN-15331
- **Date:** 2022-01-13
- **CVE:** CVE-2022-21895
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Abdelhamid Naceri
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-050/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the User Profile Service. By creating a directory junction, an attacker can abuse the service to delete a file. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-21895

## Disclosure Timeline

- 2021-10-06 - Vulnerability reported to vendor
- 2022-01-13 - Coordinated public release of advisory
