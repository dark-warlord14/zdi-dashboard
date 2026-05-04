# ZDI-22-1162: ICONICS GENESIS64 GDFX File Parsing Path Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1162
- **ZDI-CAN:** ZDI-CAN-17360
- **Date:** 2022-08-23
- **CVE:** CVE-2022-33317
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** ICONICS
- **Affected Products:** GENESIS64
- **Credit:** Noam Moshe of Claroty Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1162/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of ICONICS GENESIS64. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of GDFX files. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of the ICONICS_ADMIN user.

## Additional Details

ICONICS has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/uscert/ics/advisories/icsa-22-202-04

## Disclosure Timeline

- 2022-07-19 - Vulnerability reported to vendor
- 2022-08-23 - Coordinated public release of advisory
