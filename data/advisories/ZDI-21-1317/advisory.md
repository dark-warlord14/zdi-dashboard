# ZDI-21-1317: (0Day) Autodesk Design Review PDF File Parsing Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1317
- **ZDI-CAN:** ZDI-CAN-14243
- **Date:** 2021-11-17
- **CVE:** CVE-2021-27038
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Autodesk
- **Affected Products:** Design Review
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1317/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Autodesk Design Review. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of PDF files. The issue results from the lack of proper validation of user-supplied data, which can result in a type confusion condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 06/29/21 - ZDI reported the vulnerabilities to the vendor 06/29/21 - The vendor confirmed receipt of the reports 10/05/21 - ZDI requested an update 10/20/21 - The vendor communicated that the issues would be fixed on 10/23/21 10/29/21 - The vendor requested an extension 11/05/21 - ZDI requested the disclosure date 11/08/21 - The vendor indicated that the issues would be fixed before the end of the year 11/09/21 - ZDI notified the vendor of the intention to publish these reports as 0-day advisories on 11/17/21 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application. https://www.autodesk.com/trust/security-advisories/adsk-sa-2022-0004

## Disclosure Timeline

- 2021-06-25 - Vulnerability reported to vendor
- 2021-11-17 - Coordinated public release of advisory
- 2022-01-21 - Advisory Updated
