# ZDI-25-601: (Pwn2Own) Oracle VirtualBox VMSVGA Integer Overflow Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-601
- **ZDI-CAN:** ZDI-CAN-27122
- **Date:** 2025-07-15
- **CVE:** CVE-2025-53024
- **CVSS:** 8.2
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** Prison Break(GANGMIN KIM,SANGBIN KIM,HANSEO KIM,SANGWON OH,SANGHOON LEE, WONJOON HWANG)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-601/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Oracle VirtualBox. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the implementation of the VMSVGA virtual device. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before writing to memory. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpujul2025.html

## Disclosure Timeline

- 2025-05-21 - Vulnerability reported to vendor
- 2025-07-15 - Coordinated public release of advisory
- 2025-07-15 - Advisory Updated
