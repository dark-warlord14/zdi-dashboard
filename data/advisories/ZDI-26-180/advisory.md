# ZDI-26-180: Microsoft Windows cdd Improper Locking Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-180
- **ZDI-CAN:** ZDI-CAN-28247
- **Date:** 2026-03-10
- **CVE:** CVE-2026-23668
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Marcin Wiazowski
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-180/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the cdd.dll driver. The issue results from the lack of proper locking when performing operations on an object. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-23668

## Disclosure Timeline

- 2025-12-02 - Vulnerability reported to vendor
- 2026-03-10 - Coordinated public release of advisory
- 2026-03-10 - Advisory Updated
