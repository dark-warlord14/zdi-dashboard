# ZDI-25-693: Norton Utilities Ultimate NortonUtilitiesSvc Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-693
- **ZDI-CAN:** ZDI-CAN-25570
- **Date:** 2025-07-29
- **CVE:** CVE-2024-13944
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Norton
- **Affected Products:** Norton Utilities Ultimate
- **Credit:** Vladislav Berghici of Trend Micro Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-693/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Norton Utilities Ultimate. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Norton Utilities Service. By creating a symbolic link, an attacker can abuse the service to delete arbitrary files. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Fixed in Norton Utilities 24.3 SU1 - 24.3.17165.6812

## Disclosure Timeline

- 2024-11-05 - Vulnerability reported to vendor
- 2025-07-29 - Coordinated public release of advisory
- 2025-07-29 - Advisory Updated
