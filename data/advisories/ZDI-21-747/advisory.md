# ZDI-21-747: Autodesk Design Review PDF File Parsing Double Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-747
- **ZDI-CAN:** ZDI-CAN-12913
- **Date:** 2021-06-22
- **CVE:** CVE-2021-27033
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Autodesk
- **Affected Products:** Design Review
- **Credit:** xina1i at SecZone
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-747/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Autodesk Design Review. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of PDF files. The issue results from the lack of validating the existence of an object prior to performing further free operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Autodesk has issued an update to correct this vulnerability. More details can be found at: https://www.autodesk.com/trust/security-advisories/adsk-sa-2021-0003

## Disclosure Timeline

- 2021-02-25 - Vulnerability reported to vendor
- 2021-06-22 - Coordinated public release of advisory
