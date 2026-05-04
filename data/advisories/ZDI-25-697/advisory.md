# ZDI-25-697: AVG TuneUp for PC TuneupSvc Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-697
- **ZDI-CAN:** ZDI-CAN-25498
- **Date:** 2025-07-29
- **CVE:** CVE-2024-13959
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** AVG
- **Affected Products:** TuneUp for PC
- **Credit:** Vladislav Berghici of Trend Micro Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-697/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of AVG TuneUp for PC. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the AVG TuneUp Service. By creating a symbolic link, an attacker can abuse the service to delete a directory. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Fixed in AVG TuneUp 24.3.17165.10564

## Disclosure Timeline

- 2024-10-03 - Vulnerability reported to vendor
- 2025-07-29 - Coordinated public release of advisory
- 2025-07-29 - Advisory Updated
