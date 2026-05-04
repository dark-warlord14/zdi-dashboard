# ZDI-25-884: QEMU uefi-vars Uninitialized Memory Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-884
- **ZDI-CAN:** ZDI-CAN-27261
- **Date:** 2025-09-04
- **CVE:** CVE-2025-8860
- **CVSS:** 5.3
- **CVSS Vector:** AV:L/AC:H/PR:H/UI:N/S:C/C:H/I:N/A:N
- **Affected Vendors:** QEMU
- **Affected Products:** QEMU
- **Credit:** Xiaobye(@xiaobye_tw) of DEVCORE Research Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-884/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of QEMU. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the uefi-vars device. The issue results from the lack of proper initialization of memory prior to accessing it. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the emulator.

## Additional Details

QEMU has issued an update to correct this vulnerability. More details can be found at: https://bugzilla.redhat.com/show_bug.cgi?id=2387588

## Disclosure Timeline

- 2025-07-18 - Vulnerability reported to vendor
- 2025-09-04 - Coordinated public release of advisory
- 2025-09-04 - Advisory Updated
