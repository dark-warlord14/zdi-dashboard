# ZDI-24-995: Linux Kernel Netfilter Conntrack Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-995
- **ZDI-CAN:** ZDI-CAN-21202
- **Date:** 2024-07-29
- **CVE:** CVE-2023-39197
- **CVSS:** 4.0
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:C/C:L/I:N/A:N
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Lucas Leong (@_wmliang_) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-995/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Linux Kernel. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of the DCCP protocol. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated data structure. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the kernel.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://access.redhat.com/security/cve/CVE-2023-39197

## Disclosure Timeline

- 2023-05-19 - Vulnerability reported to vendor
- 2024-07-29 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
