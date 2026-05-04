# ZDI-26-232: (Pwn2Own) Red Hat Enterprise Linux vmwgfx Driver Integer Overflow Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-232
- **ZDI-CAN:** ZDI-CAN-27173
- **Date:** 2026-03-30
- **CVE:** CVE-2025-40277
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Red Hat
- **Affected Products:** Enterprise Linux
- **Credit:** Pumpkin (@u1f383) from DEVCORE Research Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-232/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Red Hat Enterprise Linux. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the vmw_cmd_check function. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before writing to memory. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the kernel.

## Additional Details

Red Hat has issued an update to correct this vulnerability. More details can be found at: https://access.redhat.com/security/cve/cve-2025-40277

## Disclosure Timeline

- 2025-05-29 - Vulnerability reported to vendor
- 2026-03-30 - Coordinated public release of advisory
- 2026-03-30 - Advisory Updated
