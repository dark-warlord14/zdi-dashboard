# ZDI-24-1723: (0Day) Delta Electronics DRASimuCAD ICS File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1723
- **ZDI-CAN:** ZDI-CAN-22415
- **Date:** 2024-12-20
- **CVE:** CVE-2024-12835
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Delta Electronics
- **Affected Products:** DRASimuCAD
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1723/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Delta Electronics DRASimuCAD. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of ICS files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

07/16/24 – ZDI reported the vulnerability to ICS-CERT 08/07/24 – the vendor acknowledged the receipt of the report 11/07/24 - ZDI asked for updates 11/21/24 – the vendor communicated that the fix will be released in January 2025 11/28/24 - ZDI notified the vendor of the intention to publish the case as a 0-day advisory Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application

## Disclosure Timeline

- 2024-07-12 - Vulnerability reported to vendor
- 2024-12-20 - Coordinated public release of advisory
- 2024-12-20 - Advisory Updated
