# ZDI-22-722: (0Day) Autodesk Navisworks Manage SKP File Parsing Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-722
- **ZDI-CAN:** ZDI-CAN-16042
- **Date:** 2022-05-10
- **CVE:** N/A
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Autodesk
- **Affected Products:** Navisworks Manage
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-722/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Autodesk Navisworks Manage. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of SKP files. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 11/19/21 – ZDI reported the vulnerabilities to the vendor 11/19/21 – The vendor acknowledged the report 03/09/22 – The vendor requested an extension until 04/01/22 03/09/22 – ZDI approved an extension until 04/01/22 04/01/22 – ZDI requested an update 04/01/22 – The vendor clarified that the issues have not been fixed 04/22/22 – ZDI notified the vendor of the intention to publish the cases as 0-day advisories on 04/28/22 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2021-11-19 - Vulnerability reported to vendor
- 2022-05-10 - Coordinated public release of advisory
- 2022-05-10 - Advisory Updated
