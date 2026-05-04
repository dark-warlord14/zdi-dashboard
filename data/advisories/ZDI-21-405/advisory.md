# ZDI-21-405: (0Day) Microsoft Print 3D PLY File Parsing Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-405
- **ZDI-CAN:** ZDI-CAN-12876
- **Date:** 2021-04-13
- **CVE:** N/A
- **CVSS:** 6.6
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:L/A:L
- **Affected Vendors:** Microsoft
- **Affected Products:** Print 3D
- **Credit:** garmin
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-405/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Print 3D. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of PLY files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated data structure. An attacker can leverage this vulnerability to execute code in the context of the current process at low integrity.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 02/02/21 – ZDI reported the vulnerability to the vendor 02/06/21 – The vendor acknowledged the report 02/11/21 – The vendor claimed they believed the issue to be not exploitable 02/11/21 – ZDI provided additional evidence 02/11/21 – The vendor claimed they believed the issue to be not exploitable 02/12/21 – ZDI provided additional evidence 02/16/21 – The vendor requested technical clarification 02/26/21 – ZDI provided additional evidence 03/24/21 – The vendor reported the case was considered low-severity and it would be closed 03/25/21 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory 03/31/21 – ZDI notified ICS-CERT of the intention to publish the case as a 0-day advisory on 04/13/21 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2021-02-02 - Vulnerability reported to vendor
- 2021-04-13 - Coordinated public release of advisory
