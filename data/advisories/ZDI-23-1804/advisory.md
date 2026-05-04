# ZDI-23-1804: Parallels Desktop virtio-gpu Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1804
- **ZDI-CAN:** ZDI-CAN-21260
- **Date:** 2023-12-19
- **CVE:** CVE-2023-50227
- **CVSS:** 8.3
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:R/S:C/C:H/I:H/A:H
- **Affected Vendors:** Parallels
- **Affected Products:** Desktop
- **Credit:** pwn2car
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1804/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Parallels Desktop. User interaction is required to exploit this vulnerability in that the target in a guest system must visit a malicious page or open a malicious file. The specific flaw exists within the virtio-gpu virtual device. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the hypervisor.

## Additional Details

Parallels has issued an update to correct this vulnerability. More details can be found at: https://kb.parallels.com/en/125013

## Disclosure Timeline

- 2023-09-05 - Vulnerability reported to vendor
- 2023-12-19 - Coordinated public release of advisory
