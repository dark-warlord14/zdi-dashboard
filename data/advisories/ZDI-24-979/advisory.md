# ZDI-24-979: Microsoft Office Visio DXF File Parsing Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-979
- **ZDI-CAN:** ZDI-CAN-19066
- **Date:** 2024-07-29
- **CVE:** N/A
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Visio
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-979/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Office Visio. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of DXF files. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before writing to memory. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fixed in Version 16.0.17628.20144

## Disclosure Timeline

- 2022-10-04 - Vulnerability reported to vendor
- 2024-07-29 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
