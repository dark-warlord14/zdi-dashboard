# ZDI-24-1696: libarchive RAR File Parsing Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1696
- **ZDI-CAN:** ZDI-CAN-23729
- **Date:** 2024-12-19
- **CVE:** CVE-2024-20697
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** libarchive
- **Affected Products:** libarchive
- **Credit:** Guy Lederfein of Trend Micro Security Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1696/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of libarchive. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of RAR files. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before writing to memory. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

libarchive has issued an update to correct this vulnerability. More details can be found at: https://github.com/libarchive/libarchive/pull/2135

## Disclosure Timeline

- 2024-04-17 - Vulnerability reported to vendor
- 2024-12-19 - Coordinated public release of advisory
- 2024-12-19 - Advisory Updated
