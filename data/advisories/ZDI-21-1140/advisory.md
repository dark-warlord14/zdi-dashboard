# ZDI-21-1140: Autodesk Design Review PICT File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1140
- **ZDI-CAN:** ZDI-CAN-14255
- **Date:** 2021-10-06
- **CVE:** CVE-2021-27035
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Autodesk
- **Affected Products:** Design Review
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1140/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Autodesk Design Review. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of PICT files. Crafted data in a PICT file can trigger a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Autodesk has issued an update to correct this vulnerability. More details can be found at: https://www.autodesk.com/trust/security-advisories/adsk-sa-2021-0003

## Disclosure Timeline

- 2021-06-25 - Vulnerability reported to vendor
- 2021-10-06 - Coordinated public release of advisory
