# ZDI-21-1065: (0Day) Autodesk Navisworks DWG File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1065
- **ZDI-CAN:** ZDI-CAN-13719
- **Date:** 2021-09-14
- **CVE:** CVE-2021-40156
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Autodesk
- **Affected Products:** Navisworks
- **Credit:** Michael DePlante (@izobashi) of Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1065/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Autodesk Navisworks. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of DWG files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 04/23/21 - ZDI reported the vulnerabilities to the vendor 04/29/21 - The vendor confirmed receipt of the reports and requested technical clarification 05/04/21 - ZDI confirmed that the requested details were provided in the reports 05/21/21 - The vendor communicated that the vulnerabilities affect a third-party component 08/16/21 - The vendor requested an extension 08/16/21 - ZDI agreed to an extension until 09/01/2021 08/17/21 - The vendor requested an extension until 09/13/21 08/17/21 - ZDI agreed to an extension until 09/13/2021 08/25/21 - The vendor requested an extension until 10/01/21 08/26/21 - ZDI notified the vendor of the intention to publish these reports as 0-day advisories on 09/13/2021 9/13/21 - The vendor published a fix ( https://www.autodesk.com/trust/security-advisories/adsk-sa-2021-0009 ) -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2021-04-22 - Vulnerability reported to vendor
- 2021-09-14 - Coordinated public release of advisory
- 2021-09-15 - Advisory Updated
