# ZDI-25-1136: GIMP PNM File Parsing Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1136
- **ZDI-CAN:** ZDI-CAN-28273
- **Date:** 2025-12-17
- **CVE:** CVE-2025-14422
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** GIMP
- **Affected Products:** GIMP
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1136/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of GIMP. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of PNM files. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before allocating a buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

GIMP has issued an update to correct this vulnerability. More details can be found at: https://gitlab.gnome.org/GNOME/gimp/-/commit/4ff2d773d58064e6130495de498e440f4a6d5edb

## Disclosure Timeline

- 2025-11-11 - Vulnerability reported to vendor
- 2025-12-17 - Coordinated public release of advisory
- 2025-12-17 - Advisory Updated
