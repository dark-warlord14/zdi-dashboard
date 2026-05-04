# ZDI-21-777: (0Day) Autodesk Design Review PDF File Parsing Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-777
- **ZDI-CAN:** ZDI-CAN-12984
- **Date:** 2021-07-07
- **CVE:** CVE-2021-27035
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Autodesk
- **Affected Products:** Design Review
- **Credit:** xina1i at SecZone
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-777/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Autodesk Design Review. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of PDF files. Crafted data in a PDF file can trigger a read past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 02/10/21 - ZDI reported the vulnerability to the vendor 03/15/21 - The vendor requested technical clarification 03/18/21 - ZDI provided additional evidence 06/04/21 - The vendor confirmed that the advisory would be published by 06/18/2021 06/18/21 - ZDI requested the advisory link 06/18/21 - The vendor communicated that the issue couldn’t be fixed due the inability to update an old third party library 06/18/21 - ZDI notified the vendor of the intention to publish this report as a 0-day advisory on 06/29/21 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application. https://www.autodesk.com/trust/security-advisories/adsk-sa-2022-0004

## Disclosure Timeline

- 2021-02-10 - Vulnerability reported to vendor
- 2021-07-07 - Coordinated public release of advisory
- 2022-01-21 - Advisory Updated
