# ZDI-25-910: GIMP HDR File Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-910
- **ZDI-CAN:** ZDI-CAN-27803
- **Date:** 2025-09-24
- **CVE:** CVE-2025-10921
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** GIMP
- **Affected Products:** GIMP
- **Credit:** MICHAEL RANDRIANANTENAINA [https://elkamika.blogspot.com/]
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-910/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of GIMP. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of HDR files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

GIMP has issued an update to correct this vulnerability. More details can be found at: https://gitlab.gnome.org/GNOME/gegl/-/commit/0e68b7471dabf2800d780819c19bd5e6462f565f

## Disclosure Timeline

- 2025-09-02 - Vulnerability reported to vendor
- 2025-09-24 - Coordinated public release of advisory
- 2025-09-24 - Advisory Updated
