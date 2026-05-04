# ZDI-23-483: (Pwn2Own) Oracle VirtualBox VGA MMIO Handling Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-483
- **ZDI-CAN:** ZDI-CAN-20669
- **Date:** 2023-04-24
- **CVE:** CVE-2023-21991
- **CVSS:** 6.0
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:N/A:N
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** Bien Pham (@bienpnn) from Qrious Security (@qriousec)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-483/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Oracle VirtualBox. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the handling of VGA MMIO. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpuapr2023.html

## Disclosure Timeline

- 2023-03-30 - Vulnerability reported to vendor
- 2023-04-24 - Coordinated public release of advisory
