# ZDI-25-321: GIMP ICO File Parsing Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-321
- **ZDI-CAN:** ZDI-CAN-26752
- **Date:** 2025-06-03
- **CVE:** CVE-2025-5473
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** GIMP
- **Affected Products:** GIMP
- **Credit:** MICHAEL RANDRIANANTENAINA [https://elkamika.blogspot.com/]
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-321/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of GIMP. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of ICO files. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before writing to memory. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

GIMP has issued an update to correct this vulnerability. More details can be found at: https://www.gimp.org/news/2025/05/18/gimp-3-0-4-released/#general-bugfixes

## Disclosure Timeline

- 2025-04-25 - Vulnerability reported to vendor
- 2025-06-03 - Coordinated public release of advisory
- 2025-06-06 - Advisory Updated
