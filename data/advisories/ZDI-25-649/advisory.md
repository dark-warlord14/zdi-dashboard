# ZDI-25-649: Veeam Agent for Microsoft Windows Incorrect Default Permissions Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-649
- **ZDI-CAN:** ZDI-CAN-25685
- **Date:** 2025-07-24
- **CVE:** CVE-2025-24287
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Veeam
- **Affected Products:** Veeam Agent for Microsoft Windows
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-649/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Veeam Agent for Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the product installer. The issue results from incorrect permissions on a file used by the product. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Veeam has issued an update to correct this vulnerability. More details can be found at: https://www.veeam.com/kb4743

## Disclosure Timeline

- 2025-03-10 - Vulnerability reported to vendor
- 2025-07-24 - Coordinated public release of advisory
- 2025-07-24 - Advisory Updated
