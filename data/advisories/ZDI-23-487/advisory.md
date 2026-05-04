# ZDI-23-487: (Pwn2Own) Oracle VirtualBox TPM MMIO Handling Stack-based Buffer Overflow Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-487
- **ZDI-CAN:** ZDI-CAN-20779
- **Date:** 2023-04-24
- **CVE:** CVE-2023-21987
- **CVSS:** 8.2
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** Bien Pham (@bienpnn) from Qrious Security (@qriousec)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-487/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Oracle VirtualBox. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the handling of TPM MMIO. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpuapr2023.html

## Disclosure Timeline

- 2023-03-30 - Vulnerability reported to vendor
- 2023-04-24 - Coordinated public release of advisory
