# ZDI-21-816: Cisco WebEx Network Recording Player ARF File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-816
- **ZDI-CAN:** ZDI-CAN-13456
- **Date:** 2021-07-19
- **CVE:** N/A
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Cisco
- **Affected Products:** WebEx
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-816/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Cisco WebEx Network Recording Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of ARF files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Fixed in version 41.5.0

## Disclosure Timeline

- 2021-03-17 - Vulnerability reported to vendor
- 2021-07-19 - Coordinated public release of advisory
