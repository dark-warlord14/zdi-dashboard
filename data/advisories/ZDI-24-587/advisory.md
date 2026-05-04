# ZDI-24-587: Linux Kernel ksmbd SetInfo Request Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-587
- **ZDI-CAN:** ZDI-CAN-21598
- **Date:** 2024-06-10
- **CVE:** N/A
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:C/C:H/I:N/A:N
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Pumpkin
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-587/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Linux Kernel. Authentication is not required to exploit this vulnerability. However, only systems with ksmbd enabled are vulnerable. The specific flaw exists within the parsing of SMB2 SetInfo requests. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the kernel.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://lore.kernel.org/all/20230813211710.859658800@linuxfoundation.org/

## Disclosure Timeline

- 2023-08-02 - Vulnerability reported to vendor
- 2024-06-10 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
