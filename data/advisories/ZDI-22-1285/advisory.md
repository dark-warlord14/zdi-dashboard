# ZDI-22-1285: Microsoft Windows Group Policy Preference Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1285
- **ZDI-CAN:** ZDI-CAN-17112
- **Date:** 2022-09-19
- **CVE:** CVE-2022-37955
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** @decoder_it
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1285/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. This vulnerability is dependent upon a Group Policy setting, and an attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Group Policy Preference Client module. By creating a symbolic link, an attacker can cause the module to create an arbitrary file. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-37955

## Disclosure Timeline

- 2022-06-07 - Vulnerability reported to vendor
- 2022-09-19 - Coordinated public release of advisory
