# ZDI-25-972: Krita TGA File Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-972
- **ZDI-CAN:** ZDI-CAN-27830
- **Date:** 2025-10-27
- **CVE:** CVE-2025-59820
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Krita
- **Affected Products:** Krita
- **Credit:** MICHAEL RANDRIANANTENAINA [https://elkamika.blogspot.com/]
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-972/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Krita. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of TGA files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Krita has issued an update to correct this vulnerability. More details can be found at: https://kde.org/info/security/advisory-20250929-1.txt

## Disclosure Timeline

- 2025-09-05 - Vulnerability reported to vendor
- 2025-10-27 - Coordinated public release of advisory
- 2025-10-27 - Advisory Updated
