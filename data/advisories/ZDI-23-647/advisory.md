# ZDI-23-647: Apple Safari PDFPluginAnnotation Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-647
- **ZDI-CAN:** ZDI-CAN-17338
- **Date:** 2023-05-17
- **CVE:** CVE-2022-32922
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** Yonghwi Jin (@jinmo123) at Theori
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-647/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of PDFPluginAnnotation objects. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/HT213489

## Disclosure Timeline

- 2022-07-07 - Vulnerability reported to vendor
- 2023-05-17 - Coordinated public release of advisory
