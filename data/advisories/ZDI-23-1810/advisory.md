# ZDI-23-1810: QEMU NVMe Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1810
- **ZDI-CAN:** ZDI-CAN-21521
- **Date:** 2023-12-20
- **CVE:** CVE-2023-4135
- **CVSS:** 6.0
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:N/A:N
- **Affected Vendors:** QEMU
- **Affected Products:** QEMU
- **Credit:** Pumpkin (@u1f383)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1810/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of QEMU. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the NVMe virtual device. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the hypervisor.

## Additional Details

QEMU has issued an update to correct this vulnerability. More details can be found at: https://access.redhat.com/security/cve/CVE-2023-4135

## Disclosure Timeline

- 2023-08-02 - Vulnerability reported to vendor
- 2023-12-20 - Coordinated public release of advisory
