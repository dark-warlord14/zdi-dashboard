# ZDI-23-980: Linux Kernel ksmbd Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-980
- **ZDI-CAN:** ZDI-CAN-21164
- **Date:** 2023-07-28
- **CVE:** CVE-2023-3865
- **CVSS:** 7.1
- **CVSS Vector:** AV:N/AC:H/PR:L/UI:N/S:C/C:L/I:N/A:H
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** 8437438cb38d8565e9a990474a7b8d2b3e3770a521eb159325e93c6189f526d1
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-980/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Linux Kernel. Authentication may or may not be required to exploit this vulnerability, depending upon configuration. Furthermore, only systems with ksmbd enabled are vulnerable. The specific flaw exists within the parsing of smb2_hdr structure. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the kernel.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://lore.kernel.org/all/20230626180806.056931954@linuxfoundation.org/

## Disclosure Timeline

- 2023-06-13 - Vulnerability reported to vendor
- 2023-07-28 - Coordinated public release of advisory
- 2024-04-17 - Advisory Updated
