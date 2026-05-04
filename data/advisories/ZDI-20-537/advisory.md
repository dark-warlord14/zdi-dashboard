# ZDI-20-537: (Pwn2Own) Amazon Echo Show Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-537
- **ZDI-CAN:** ZDI-CAN-9644
- **Date:** 2020-04-16
- **CVE:** N/A
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Amazon
- **Affected Products:** Echo Show
- **Credit:** fluoroacetate
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-537/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Amazon Echo Show. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of arrays. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before allocating a buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fixed in version 3523856004

## Disclosure Timeline

- 2019-12-10 - Vulnerability reported to vendor
- 2020-04-16 - Coordinated public release of advisory
