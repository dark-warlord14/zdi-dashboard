# ZDI-21-1537: Tencent WeChat WXAM Decoder Uninitialized Pointer Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1537
- **ZDI-CAN:** ZDI-CAN-13813
- **Date:** 2021-12-14
- **CVE:** N/A
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Tencent
- **Affected Products:** WeChat
- **Credit:** Lucas Leong (@_wmliang_) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1537/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Tencent WeChat. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the WXAM decoder. The issue results from the lack of proper initialization of a pointer prior to accessing it. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fixed in version 8.0.14

## Disclosure Timeline

- 2021-05-12 - Vulnerability reported to vendor
- 2021-12-14 - Coordinated public release of advisory
