# ZDI-25-960: Oracle VirtualBox VMSVGA Stack-based Buffer Overflow Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-960
- **ZDI-CAN:** ZDI-CAN-27924
- **Date:** 2025-10-27
- **CVE:** CVE-2025-62590
- **CVSS:** 8.2
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** VMBreakers(GANGMIN KIM, SANGBIN KIM, Un3xploitable)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-960/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Oracle VirtualBox. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the VMSVGA device. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpuoct2025.html

## Disclosure Timeline

- 2025-09-25 - Vulnerability reported to vendor
- 2025-10-27 - Coordinated public release of advisory
- 2025-10-27 - Advisory Updated
