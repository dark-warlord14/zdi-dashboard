# ZDI-25-203: GIMP XWD File Parsing Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-203
- **ZDI-CAN:** ZDI-CAN-25082
- **Date:** 2025-04-07
- **CVE:** CVE-2025-2760
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** GIMP
- **Affected Products:** GIMP
- **Credit:** MICHAEL RANDRIANANTENAINA [https://elkamika.blogspot.com/]
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-203/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of GIMP. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of XWD files. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before allocating a buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fixed in GIMP 3.0.0 https://www.gimp.org/news/2025/03/16/gimp-3-0-released

## Disclosure Timeline

- 2025-01-22 - Vulnerability reported to vendor
- 2025-04-07 - Coordinated public release of advisory
- 2025-04-07 - Advisory Updated
