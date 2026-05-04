# ZDI-21-506: Microsoft Windows Raw Image Extension X3F File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-506
- **ZDI-CAN:** ZDI-CAN-12635
- **Date:** 2021-05-04
- **CVE:** N/A
- **CVSS:** 5.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:L
- **Affected Vendors:** Microsoft
- **Affected Products:** Raw Image Extension
- **Credit:** Hossein Lotfi of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-506/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Raw Image Extension. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the msrawimage_store module. Crafted data in an X3F file can trigger a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current user at low integrity.

## Additional Details

Fixed in version 1.0.40392.0

## Disclosure Timeline

- 2020-12-04 - Vulnerability reported to vendor
- 2021-05-04 - Coordinated public release of advisory
