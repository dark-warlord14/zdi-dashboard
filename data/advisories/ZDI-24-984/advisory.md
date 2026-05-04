# ZDI-24-984: Microsoft Word DOC File Parsing Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-984
- **ZDI-CAN:** ZDI-CAN-18535
- **Date:** 2024-07-29
- **CVE:** N/A
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Word
- **Credit:** Hossein Lotfi of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-984/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Word. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of DOC files. Crafted data in a DOC file can cause a pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fixed in version 16.0.17231.20236

## Disclosure Timeline

- 2022-08-25 - Vulnerability reported to vendor
- 2024-07-29 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
