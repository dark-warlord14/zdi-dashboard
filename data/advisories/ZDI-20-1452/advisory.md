# ZDI-20-1452: (0Day) Microsoft 3D Builder GLB File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1452
- **ZDI-CAN:** ZDI-CAN-11486
- **Date:** 2020-12-21
- **CVE:** N/A
- **CVSS:** 6.6
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:L/A:L
- **Affected Vendors:** Microsoft
- **Affected Products:** 3D Builder
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1452/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft 3D Builder. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of GLB files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated data structure. An attacker can leverage this vulnerability to execute code in the context of the current process at low integrity.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 07/02/20 - ZDI reported the vulnerability to Microsoft 07/02/20 - Microsoft confirmed receipt of the report 07/24/20 - Microsoft confirmed the reported behavior 10/09/20 - ZDI requested a status update 12/14/20 - ZDI requested a status update 12/15/20 - ZDI notified Microsoft of the intention to publish the report as 0-day advisory on 12/21/20 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2020-07-02 - Vulnerability reported to vendor
- 2020-12-21 - Coordinated public release of advisory
- 2021-02-03 - Advisory Updated
