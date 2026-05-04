# ZDI-24-778: Linux Kernel USB Core Out-Of-Bounds Read Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-778
- **ZDI-CAN:** ZDI-CAN-22042
- **Date:** 2024-06-14
- **CVE:** N/A
- **CVSS:** 7.1
- **CVSS Vector:** AV:P/AC:H/PR:N/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Lucas Leong (@_wmliang_) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-778/
## Vulnerability Details

This vulnerability allows physically present attackers to escalate privileges on affected installations of Linux Kernel. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of USB descriptors. The issue results from the lack of proper validation of user-supplied data, which can result in a memory read past the end of an allocated buffer. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the kernel.

## Additional Details

Fixed in Linux 6.6-rc1 https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=ff33299ec8bb80cdcc073ad9c506bd79bb2ed20b

## Disclosure Timeline

- 2023-08-29 - Vulnerability reported to vendor
- 2024-06-14 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
