# ZDI-21-963: Microsoft Windows Update Service Incorrect Permission Assignment Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-963
- **ZDI-CAN:** ZDI-CAN-13457
- **Date:** 2021-08-11
- **CVE:** CVE-2021-26431
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Abdelhamid Naceri (halov)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-963/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Windows Update service. The issue results from incorrect permissions set on a directory. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-26431

## Disclosure Timeline

- 2021-04-22 - Vulnerability reported to vendor
- 2021-08-11 - Coordinated public release of advisory
