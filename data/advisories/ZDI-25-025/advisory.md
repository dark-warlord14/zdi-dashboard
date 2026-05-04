# ZDI-25-025: Avira Prime System Speedup Service Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-025
- **ZDI-CAN:** ZDI-CAN-22247
- **Date:** 2025-01-09
- **CVE:** CVE-2024-9525
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Avira
- **Affected Products:** Prime
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-025/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Avira Prime. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the System Speedup Service. By creating a symbolic link, an attacker can abuse the service to delete a file. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Fixed in Speedup 6.27

## Disclosure Timeline

- 2024-05-16 - Vulnerability reported to vendor
- 2025-01-09 - Coordinated public release of advisory
- 2025-01-09 - Advisory Updated
