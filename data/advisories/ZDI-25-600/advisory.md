# ZDI-25-600: (Pwn2Own) Oracle VirtualBox VMSVGA Out-Of-Bounds Write Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-600
- **ZDI-CAN:** ZDI-CAN-27163
- **Date:** 2025-07-15
- **CVE:** CVE-2025-53028
- **CVSS:** 8.2
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** Viettel Cyber Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-600/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Oracle VirtualBox. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the implemetation of the VMSVGA virtual device. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpujul2025.html

## Disclosure Timeline

- 2025-05-21 - Vulnerability reported to vendor
- 2025-07-15 - Coordinated public release of advisory
- 2025-07-15 - Advisory Updated
