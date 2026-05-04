# ZDI-25-473: Parallels Client Uncontrolled Search Path Element Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-473
- **ZDI-CAN:** ZDI-CAN-25039
- **Date:** 2025-07-07
- **CVE:** CVE-2025-6812
- **CVSS:** 7.3
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Parallels
- **Affected Products:** Client
- **Credit:** Kolja Grassmann (Neodyme)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-473/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Parallels Client. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the AppServer service. The service loads an OpenSSL configuration file from an unsecured location. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of a target user.

## Additional Details

Fixed in: *Parallels Client (Windows) v20.2-25889 *Parallels RAS Core v19.4.3.2-25228 (Hotfix) *Parallels Client (Windows) v19.4.3-25221 (Hotfix) Details can be found in https://kb.parallels.com/en/129018#section7 (version 19) and https://kb.parallels.com/en/130242 (version 20)

## Disclosure Timeline

- 2024-10-15 - Vulnerability reported to vendor
- 2025-07-07 - Coordinated public release of advisory
- 2025-07-07 - Advisory Updated
