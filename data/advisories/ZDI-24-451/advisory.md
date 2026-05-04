# ZDI-24-451: Microsoft Windows Search Service Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-451
- **ZDI-CAN:** ZDI-CAN-22907
- **Date:** 2024-05-14
- **CVE:** CVE-2024-30033
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** HeeChan Kim (@heegong123) of THEORI
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-451/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Windows Search service. By creating a symbolic link, an attacker can abuse the service to delete a file. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-30033

## Disclosure Timeline

- 2024-01-23 - Vulnerability reported to vendor
- 2024-05-14 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
