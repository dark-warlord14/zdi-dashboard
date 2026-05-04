# ZDI-23-1855: (0Day) Hancom Office Word DOC File Parsing Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1855
- **ZDI-CAN:** ZDI-CAN-20384
- **Date:** 2023-12-20
- **CVE:** CVE-2023-51598
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Hancom
- **Affected Products:** Office
- **Credit:** logos
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1855/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Hancom Office Word. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of DOC files. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

05/26/23 – ZDI made multiple attempts to contact the vendor across sales and support channels, which yielded no response from the vendor. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application

## Disclosure Timeline

- 2023-11-17 - Vulnerability reported to vendor
- 2023-12-20 - Coordinated public release of advisory
