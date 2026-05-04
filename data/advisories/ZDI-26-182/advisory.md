# ZDI-26-182: Microsoft Windows win32full Improper Release Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-182
- **ZDI-CAN:** ZDI-CAN-28488
- **Date:** 2026-03-10
- **CVE:** CVE-2026-24285
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Marcin Wiazowski
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-182/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the win32kfull driver. The issue results from improper management of a reference count. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-24285

## Disclosure Timeline

- 2025-12-02 - Vulnerability reported to vendor
- 2026-03-10 - Coordinated public release of advisory
- 2026-03-10 - Advisory Updated
