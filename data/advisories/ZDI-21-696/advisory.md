# ZDI-21-696: (0Day) Microsoft Print 3D PLY File Parsing Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-696
- **ZDI-CAN:** ZDI-CAN-13050
- **Date:** 2021-06-17
- **CVE:** N/A
- **CVSS:** 6.6
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:L/A:L
- **Affected Vendors:** Microsoft
- **Affected Products:** Print 3D
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-696/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Print 3D. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of PLY files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated data structure. An attacker can leverage this vulnerability to execute code in the context of the current process at low integrity.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 02/02/21 – ZDI reported the vulnerability to the vendor 02/06/21 – The vendor acknowledged the report 02/11/21 – The vendor confirmed the issue 05/25/21 – ZDI requested an update 06/08/21 – ZDI requested an update and notified the vendor of the intention to publish the report as a 0-day advisory on 06/16/21 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2021-02-02 - Vulnerability reported to vendor
- 2021-06-17 - Coordinated public release of advisory
