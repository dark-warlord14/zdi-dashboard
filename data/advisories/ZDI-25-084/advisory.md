# ZDI-25-084: Mintty Sixel Image Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-084
- **ZDI-CAN:** ZDI-CAN-23382
- **Date:** 2025-02-05
- **CVE:** CVE-2025-1052
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Mintty
- **Affected Products:** Mintty
- **Credit:** solid-snail
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-084/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Mintty. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of sixel images. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

Fixed in Version 3.7.5 https://github.com/mintty/mintty/commit/c78ee1085f438333d5be4e3688e5d6b890c146c4

## Disclosure Timeline

- 2024-08-30 - Vulnerability reported to vendor
- 2025-02-05 - Coordinated public release of advisory
- 2025-02-05 - Advisory Updated
