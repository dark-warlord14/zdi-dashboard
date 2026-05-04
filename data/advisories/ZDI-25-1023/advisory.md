# ZDI-25-1023: VIPRE Advanced Security Incorrect Permission Assignment Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1023
- **ZDI-CAN:** ZDI-CAN-27147
- **Date:** 2025-11-26
- **CVE:** CVE-2025-13703
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** VIPRE
- **Affected Products:** Advanced Security
- **Credit:** Adam Babis
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1023/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of VIPRE Advanced Security for PC. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the product installer. The issue results from incorrect permissions on a folder. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

VIPRE has issued an update to correct this vulnerability. More details can be found at: https://success.vipre.com/home-windows-release-notes/home-windows-release-notes-20250925

## Disclosure Timeline

- 2025-06-05 - Vulnerability reported to vendor
- 2025-11-26 - Coordinated public release of advisory
- 2025-11-26 - Advisory Updated
