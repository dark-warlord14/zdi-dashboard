# ZDI-22-517: Apple Safari WebGLMultiDraw Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-517
- **ZDI-CAN:** ZDI-CAN-15747
- **Date:** 2022-03-22
- **CVE:** CVE-2022-22629
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-517/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the WebGLMultiDraw component. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT213187

## Disclosure Timeline

- 2021-12-22 - Vulnerability reported to vendor
- 2022-03-22 - Coordinated public release of advisory
- 2024-07-08 - Advisory Updated
