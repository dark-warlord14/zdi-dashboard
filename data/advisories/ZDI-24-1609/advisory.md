# ZDI-24-1609: Luxion KeyShot 3DS File Parsing Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1609
- **ZDI-CAN:** ZDI-CAN-23693
- **Date:** 2024-11-21
- **CVE:** CVE-2024-11578
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Luxion
- **Affected Products:** KeyShot
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1609/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Luxion KeyShot. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of 3DS files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Luxion has issued an update to correct this vulnerability. More details can be found at: https://download.keyshot.com/cert/ksa-655925/ksa-655925.pdf?version=1.0&_gl=1*1vzfrlf*_gcl_au*MTIxNTA2Njg4MS4xNzMxNTMwMjIx

## Disclosure Timeline

- 2024-04-26 - Vulnerability reported to vendor
- 2024-11-21 - Coordinated public release of advisory
- 2024-11-21 - Advisory Updated
