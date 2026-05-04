# ZDI-21-968: Microsoft Windows Update Assistant Incorrect Permission Assignment Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-968
- **ZDI-CAN:** ZDI-CAN-13429
- **Date:** 2021-08-11
- **CVE:** CVE-2021-36945
- **CVSS:** 7.3
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Abdelhamid Naceri (halov)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-968/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within Windows Update Assistant. The issue results from incorrect permissions set on a directory. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of Administrator.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-36945

## Disclosure Timeline

- 2021-04-14 - Vulnerability reported to vendor
- 2021-08-11 - Coordinated public release of advisory
