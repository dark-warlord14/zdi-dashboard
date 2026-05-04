# ZDI-21-909: (0Day) Microsoft 3D Viewer 3MF File Parsing Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-909
- **ZDI-CAN:** ZDI-CAN-13085
- **Date:** 2021-07-29
- **CVE:** CVE-2021-43209
- **CVSS:** 6.6
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:L/A:L
- **Affected Vendors:** Microsoft
- **Affected Products:** 3D Viewer
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-909/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft 3D Viewer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of 3MF files. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process at low integrity.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 02/02/21 – ZDI reported the vulnerability to the vendor 02/03/21 – The vendor acknowledged the report 04/16/21 – The vendor indicated the case did not meet the bar for servicing 04/23/21 – ZDI notified the vendor of the intention to publish the report as a 0-day advisory 04/27/21 – The vendor indicated that further review determined the case to meet the bar for servicing but it would not meet the original deadline 07/21/21 – ZDI requested an update and notified the vendor of the intention to publish the report as a 0-day advisory on 07/29/21 07/21/21 – The vendor indicated they were looking at the possible release date -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2021-02-02 - Vulnerability reported to vendor
- 2021-07-29 - Coordinated public release of advisory
