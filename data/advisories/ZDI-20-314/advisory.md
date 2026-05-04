# ZDI-20-314: (Pwn2Own) Samsung Q60 Smart QLED TV JavaScript Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-314
- **ZDI-CAN:** ZDI-CAN-9645
- **Date:** 2020-03-18
- **CVE:** N/A
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Samsung
- **Affected Products:** Q60 Smart QLED TV
- **Credit:** @fluoroacetate
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-314/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Samsung Q60 Smart QLED TV. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of arrays in JavaScript. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before writing to memory. An attacker can leverage this to execute code in the context of the current process.

## Additional Details

Fixed in version 1351.3

## Disclosure Timeline

- 2019-12-10 - Vulnerability reported to vendor
- 2020-03-18 - Coordinated public release of advisory
