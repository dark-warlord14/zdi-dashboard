# ZDI-24-588: Linux Kernel ksmbd Read Request Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-588
- **ZDI-CAN:** ZDI-CAN-21587
- **Date:** 2024-06-10
- **CVE:** CVE-2023-39179
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:C/C:H/I:N/A:L
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** HexRabbit (@h3xr4bb1t)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-588/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Linux Kernel. Authentication is not required to exploit this vulnerability. However, only systems with ksmbd enabled are vulnerable. The specific flaw exists within the handling of SMB2 read requests. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the kernel.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://lore.kernel.org/lkml/20230813160006.1073695-11-sashal@kernel.org/

## Disclosure Timeline

- 2023-07-18 - Vulnerability reported to vendor
- 2024-06-10 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
