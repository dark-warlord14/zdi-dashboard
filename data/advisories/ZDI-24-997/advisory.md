# ZDI-24-997: Linux Kernel CIFS Filesystem Decryption Improper Input Validation Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-997
- **ZDI-CAN:** ZDI-CAN-22869
- **Date:** 2024-07-29
- **CVE:** CVE-2024-0565
- **CVSS:** 8.3
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:R/S:C/C:H/I:H/A:H
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** fffvr
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-997/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Linux Kernel. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of SMB headers. The issue results from the lack of proper validation of user-supplied data prior to copying it to a buffer. An attacker can leverage this vulnerability to execute code in the context of the kernel.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://access.redhat.com/security/cve/CVE-2024-0565

## Disclosure Timeline

- 2023-12-20 - Vulnerability reported to vendor
- 2024-07-29 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
