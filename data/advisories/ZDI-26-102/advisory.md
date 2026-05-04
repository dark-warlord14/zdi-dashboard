# ZDI-26-102: Oracle VirtualBox VMSVGA Out-Of-Bounds Write Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-102
- **ZDI-CAN:** ZDI-CAN-27938
- **Date:** 2026-02-13
- **CVE:** CVE-2026-21957
- **CVSS:** 7.5
- **CVSS Vector:** AV:L/AC:H/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** NiNi (@terrynini38514) from DEVCORE Research Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-102/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Oracle VirtualBox. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the VMSVGA device. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpujan2026.html

## Disclosure Timeline

- 2025-09-25 - Vulnerability reported to vendor
- 2026-02-13 - Coordinated public release of advisory
- 2026-02-13 - Advisory Updated
