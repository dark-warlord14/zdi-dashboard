# ZDI-23-692: Linux Kernel IPv6 Segment Routing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-692
- **ZDI-CAN:** ZDI-CAN-18511
- **Date:** 2023-05-17
- **CVE:** CVE-2023-2860
- **CVSS:** 4.4
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Lucas Leong (@_wmliang_) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-692/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of the Linux Kernel. An attacker must first obtain the ability to execute high-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the processing of seg6 attributes. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilties to escalate privileges and execute arbitrary code in the context of the kernel.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://git.kernel.org/pub/scm/linux/kernel/git/netdev/net.git/commit/?id=84a53580c5d2

## Disclosure Timeline

- 2022-08-23 - Vulnerability reported to vendor
- 2023-05-17 - Coordinated public release of advisory
- 2023-05-26 - Advisory Updated
