# ZDI-23-981: Linux Kernel ksmbd Session Setup Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-981
- **ZDI-CAN:** ZDI-CAN-21355
- **Date:** 2023-07-20
- **CVE:** CVE-2023-3867
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:C/C:L/I:N/A:L
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** HexRabbit (@h3xr4bb1t) and Pumpkin (@u1f383)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-981/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Linux Kernel. Authentication is not required to exploit this vulnerability. However, only systems with ksmbd enabled are vulnerable. The specific flaw exists within the handling of session setup commands. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the kernel.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://lore.kernel.org/all/20230624040141.16088-1-linkinjeon@kernel.org/

## Disclosure Timeline

- 2023-06-21 - Vulnerability reported to vendor
- 2023-07-20 - Coordinated public release of advisory
- 2023-07-28 - Advisory Updated
