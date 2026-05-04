# ZDI-25-590: G DATA Total Security GDTunerSvc Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-590
- **ZDI-CAN:** ZDI-CAN-26240
- **Date:** 2025-07-11
- **CVE:** CVE-2025-2790
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** G DATA
- **Affected Products:** Total Security
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-590/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of G DATA Total Security. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the GDTunerSvc service. By creating a symbolic link, an attacker can abuse the service to delete arbitrary files. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Fixed in version 25.5.19.439

## Disclosure Timeline

- 2025-03-12 - Vulnerability reported to vendor
- 2025-07-11 - Coordinated public release of advisory
- 2025-07-11 - Advisory Updated
