# ZDI-21-787: (0Day) GoPro Player MOV File Parsing Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-787
- **ZDI-CAN:** ZDI-CAN-12562
- **Date:** 2021-07-13
- **CVE:** N/A
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** GoPro
- **Affected Products:** Player
- **Credit:** garmin
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-787/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of GoPro Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of MOV files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated structure. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 02/08/21 - ZDI reported the vulnerability to the vendor 02/09/21 - The vendor confirmed receipt of the reports 02/11/21 - The vendor requested technical clarification 02/11/21 - ZDI provided additional evidence 03/01/21 - The vendor acknowledged the behavior of the reported issue 06/16/21 - ZDI requested an update 06/18/21 - The vendor communicated that the issue had not been fixed 06/21/21 - ZDI notified the vendor of the intention to publish this report as a 0-day advisory on 06/29/21 06/24/21 - The vendor indicated they were actively working on the fix and requested technical clarification 06/30/21 - ZDI provided additional evidence 07/01/21 - The vendor indicated fixes would be ready the following week. 07/08/21 - ZDI requested an update with no reply -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2021-02-15 - Vulnerability reported to vendor
- 2021-07-13 - Coordinated public release of advisory
