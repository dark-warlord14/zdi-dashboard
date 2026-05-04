# ZDI-24-494: VMware Workstation SVGA Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-494
- **ZDI-CAN:** ZDI-CAN-23490
- **Date:** 2024-05-22
- **CVE:** CVE-2024-22268
- **CVSS:** 9.6
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:H
- **Affected Vendors:** VMware
- **Affected Products:** Workstation
- **Credit:** Pwn2car
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-494/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of VMware Workstation. User interaction is required to exploit this vulnerability in that the target in a guest system must visit a malicious page or open a malicious file. The specific flaw exists within the SVGA virtual device. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the hypervisor.

## Additional Details

VMware has issued an update to correct this vulnerability. More details can be found at: https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/24280

## Disclosure Timeline

- 2024-04-02 - Vulnerability reported to vendor
- 2024-05-22 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
