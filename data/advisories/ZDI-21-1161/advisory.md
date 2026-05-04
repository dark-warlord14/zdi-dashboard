# ZDI-21-1161: Microsoft Windows AppX Deployment Service Directory Junction Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1161
- **ZDI-CAN:** ZDI-CAN-14687
- **Date:** 2021-10-14
- **CVE:** CVE-2021-41347
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Abdelhamid Naceri
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1161/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the AppX Deployment Service. By creating a directory junction, an attacker can abuse the service to delete the contents of a chosen directory. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-41347

## Disclosure Timeline

- 2021-09-01 - Vulnerability reported to vendor
- 2021-10-14 - Coordinated public release of advisory
