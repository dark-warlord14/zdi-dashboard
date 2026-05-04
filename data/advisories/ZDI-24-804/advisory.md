# ZDI-24-804: Parallels Desktop Toolgate Heap-based Buffer Overflow Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-804
- **ZDI-CAN:** ZDI-CAN-20450
- **Date:** 2024-06-18
- **CVE:** CVE-2024-6154
- **CVSS:** 8.2
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Parallels
- **Affected Products:** Desktop
- **Credit:** war10ck
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-804/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Parallels Desktop. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the Toolgate component. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length heap-based buffer. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the current user on the host system.

## Additional Details

Vendor states the patch was rolled into a previous version of Parallels Desktop version 18.1.0.

## Disclosure Timeline

- 2023-04-06 - Vulnerability reported to vendor
- 2024-06-18 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
