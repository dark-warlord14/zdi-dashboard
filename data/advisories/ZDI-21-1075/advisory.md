# ZDI-21-1075: Microsoft Windows Update Agent Directory Junction Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1075
- **ZDI-CAN:** ZDI-CAN-13765
- **Date:** 2021-09-16
- **CVE:** CVE-2021-38634
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Abdelhamid Naceri
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1075/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within Windows Update Agent. By creating a directory junction, an attacker can abuse Windows Update Agent to delete a file. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-38634

## Disclosure Timeline

- 2021-06-08 - Vulnerability reported to vendor
- 2021-09-16 - Coordinated public release of advisory
