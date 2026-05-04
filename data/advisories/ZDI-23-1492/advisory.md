# ZDI-23-1492: Linux Kernel XFRM Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1492
- **ZDI-CAN:** ZDI-CAN-18111
- **Date:** 2023-09-29
- **CVE:** CVE-2023-39194
- **CVSS:** 3.2
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:L/I:N/A:N
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Lucas Leong (@_wmliang_) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1492/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of the Linux Kernel. An attacker must first obtain the ability to execute high-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the processing of state filters. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilties to escalate privileges and execute arbitrary code in the context of the kernel.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://github.com/torvalds/linux/commit/dfa73c17d55b921e1d4e154976de35317e43a93a

## Disclosure Timeline

- 2022-08-03 - Vulnerability reported to vendor
- 2023-09-29 - Coordinated public release of advisory
- 2023-10-02 - Advisory Updated
