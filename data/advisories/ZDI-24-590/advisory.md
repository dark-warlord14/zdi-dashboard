# ZDI-24-590: Linux Kernel ksmbd smb2_open Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-590
- **ZDI-CAN:** ZDI-CAN-21824
- **Date:** 2024-06-10
- **CVE:** CVE-2023-4458
- **CVSS:** 4.0
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:C/C:L/I:N/A:N
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** HexRabbit (@h3xr4bb1t)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-590/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Linux Kernel. Authentication may or may not be required to exploit this vulnerability, depending upon configuration. Furthermore, only systems with ksmbd enabled are vulnerable. The specific flaw exists within the parsing of extended attributes. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the kernel.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://lore.kernel.org/all/20230825144848.9034-1-linkinjeon@kernel.org/

## Disclosure Timeline

- 2023-08-17 - Vulnerability reported to vendor
- 2024-06-10 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
