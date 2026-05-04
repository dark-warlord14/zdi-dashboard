# ZDI-22-073: OpenBSD Kernel Multicast Routing Uninitialized Memory Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-073
- **ZDI-CAN:** ZDI-CAN-14540
- **Date:** 2022-01-13
- **CVE:** CVE-2021-34999
- **CVSS:** 3.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:L/I:N/A:N
- **Affected Vendors:** OpenBSD
- **Affected Products:** Kernel
- **Credit:** Reno Robert of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-073/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of OpenBSD Kernel. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the implementation of multicast routing. The issue results from the lack of proper initialization of memory prior to accessing it. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges and execute arbitrary code in the context of the kernel.

## Additional Details

Fixed in version 7.0

## Disclosure Timeline

- 2021-12-15 - Vulnerability reported to vendor
- 2022-01-13 - Coordinated public release of advisory
