# ZDI-24-1382: QEMU SCSI Use-After-Free Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1382
- **ZDI-CAN:** ZDI-CAN-23962
- **Date:** 2024-10-15
- **CVE:** CVE-2024-6519
- **CVSS:** 8.2
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** QEMU
- **Affected Products:** QEMU
- **Credit:** Cyrille Chatras
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1382/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of QEMU. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the implementation of the virtual LSI53C895A SCSI Host Bus Adapter. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the hypervisor.

## Additional Details

QEMU has issued an update to correct this vulnerability. More details can be found at: https://access.redhat.com/security/cve/CVE-2024-6519

## Disclosure Timeline

- 2024-06-12 - Vulnerability reported to vendor
- 2024-10-15 - Coordinated public release of advisory
- 2024-10-15 - Advisory Updated
