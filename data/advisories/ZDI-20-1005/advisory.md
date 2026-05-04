# ZDI-20-1005: QEMU SLiRP Networking Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1005
- **ZDI-CAN:** ZDI-CAN-10892
- **Date:** 2020-08-17
- **CVE:** CVE-2020-10756
- **CVSS:** 6.5
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:N/A:N
- **Affected Vendors:** QEMU
- **Affected Products:** QEMU
- **Credit:** ziming zhang from Codesafe Team of Legendsec at Qi'anxin Group
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1005/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on affected installations of QEMU. An attacker must first obtain the ability to execute low-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the handling of SLiRP networking. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the hypervisor.

## Additional Details

QEMU has issued an update to correct this vulnerability. More details can be found at: https://access.redhat.com/security/cve/CVE-2020-10756

## Disclosure Timeline

- 2020-04-22 - Vulnerability reported to vendor
- 2020-08-17 - Coordinated public release of advisory
