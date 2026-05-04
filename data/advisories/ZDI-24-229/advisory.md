# ZDI-24-229: Linux Kernel ksmbd Session Key Exchange Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-229
- **ZDI-CAN:** ZDI-CAN-21940
- **Date:** 2024-03-01
- **CVE:** CVE-2023-52440
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Pumpkin (@u1f383)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-229/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Linux Kernel. Authentication is not required to exploit this vulnerability, but only systems with ksmbd enabled are vulnerable. The specific flaw exists within the processing of session keys. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the kernel.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://github.com/torvalds/linux/commit/4b081ce0d830b684fdf967abc3696d1261387254

## Disclosure Timeline

- 2023-08-24 - Vulnerability reported to vendor
- 2024-03-01 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
