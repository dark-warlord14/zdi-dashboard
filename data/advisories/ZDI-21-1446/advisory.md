# ZDI-21-1446: Tencent WeChat WAXM Decoder Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1446
- **ZDI-CAN:** ZDI-CAN-13336
- **Date:** 2021-12-07
- **CVE:** N/A
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Tencent
- **Affected Products:** WeChat
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1446/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Tencent WeChat. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the WXAM Decoder. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fixed in version 8.0.10

## Disclosure Timeline

- 2021-03-31 - Vulnerability reported to vendor
- 2021-12-07 - Coordinated public release of advisory
