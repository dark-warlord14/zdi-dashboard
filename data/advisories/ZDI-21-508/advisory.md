# ZDI-21-508: Microsoft Windows Raw Image Extension 3FR File Parsing Integer Underflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-508
- **ZDI-CAN:** ZDI-CAN-12152
- **Date:** 2021-05-05
- **CVE:** N/A
- **CVSS:** 4.5
- **CVSS Vector:** AV:L/AC:H/PR:N/UI:R/S:U/C:L/I:L/A:L
- **Affected Vendors:** Microsoft
- **Affected Products:** Raw Image Extension
- **Credit:** Wen guang Jiao
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-508/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Raw Image Extension. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of 3FR images. The issue results from the lack of proper validation of user-supplied data, which can result in an integer underflow before writing to memory. An attacker can leverage this vulnerability to execute code in the context of the current user at low integrity.

## Additional Details

Fixed in version 10.0.20236.1001

## Disclosure Timeline

- 2020-10-28 - Vulnerability reported to vendor
- 2021-05-05 - Coordinated public release of advisory
