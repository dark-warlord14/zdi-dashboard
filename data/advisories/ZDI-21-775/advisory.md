# ZDI-21-775: (0Day) Autodesk Design Review DWFX File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-775
- **ZDI-CAN:** ZDI-CAN-12953
- **Date:** 2021-07-05
- **CVE:** CVE-2021-27035
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Autodesk
- **Affected Products:** Design Review
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-775/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Autodesk Design Review. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of DWFX files. Crafted data in a DWFX file can trigger a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 01/29/21 - ZDI reported the vulnerabilities to the vendor 02/02/21 - The vendor confirmed receipt of the reports 05/17/21 - The vendor requested an extension until 06/18/2021 05/20/21 - ZDI agreed to an extension until 06/18/2021 06/04/21 - The vendor confirmed that the advisory would be published by 06/18/2021 06/18/21 - ZDI requested the advisory link 06/18/21 - The vendor communicated that the issues couldn’t be fixed due to external dependency to a library 06/21/21 - ZDI notified the vendor of the intention to publish these reports as a 0-day advisories on 06/29/21 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application. https://www.autodesk.com/trust/security-advisories/adsk-sa-2022-0004

## Disclosure Timeline

- 2021-01-29 - Vulnerability reported to vendor
- 2021-07-05 - Coordinated public release of advisory
- 2022-01-21 - Advisory Updated
