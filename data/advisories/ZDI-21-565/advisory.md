# ZDI-21-565: (0Day) Siemens Solid Edge Viewer PRT File Parsing Untrusted Pointer Dereference Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-565
- **ZDI-CAN:** ZDI-CAN-11962
- **Date:** 2021-05-12
- **CVE:** CVE-2021-27496
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Siemens
- **Affected Products:** Solid Edge Viewer
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-565/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Siemens Solid Edge Viewer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of PRT files. The issue results from the lack of proper validation of a user-supplied value prior to dereferencing it as a pointer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 10/21/20 - ZDI reported the vulnerabilities to ICS-CERT 10/22/20 - ICS-CERT confirmed receipt of the reports 11/23/20 - ICS-CERT communicated that the issue is in a third-party component 02/24/21 - ZDI requested an update 02/25/21 - ICS-CERT confirmed that the vendor was working on a fix 03/18/21 - ZDI requested an update 03/18/21 - ICS-CERT requested an extension 03/22/21 - ZDI agreed to an extension until 04/13/21 04/14/21 - ZDI requested an update 04/27/21 - ZDI requested an update 05/03/21 - ICS-CERT requested an extension until 05/25/21 05/04/21 - ZDI notified ICS-CERT of the intention to publish these reports as 0-day advisories on 05/12/21 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2020-10-21 - Vulnerability reported to vendor
- 2021-05-12 - Coordinated public release of advisory
