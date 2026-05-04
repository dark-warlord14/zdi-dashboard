# ZDI-25-475: (0Day) INVT HMITool VPM File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-475
- **ZDI-CAN:** ZDI-CAN-25045
- **Date:** 2025-07-07
- **CVE:** CVE-2025-7224
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** INVT
- **Affected Products:** HMITool
- **Credit:** Andrea Micalizzi aka rgod (@rgod777)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-475/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of INVT HMITool. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of VPM files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

08/15/24 – ZDI requested the vendor’s PSIRT contacts via an email to the support team 11/13/24 – ZDI asked for updates 03/11/25 – ZDI submitted the report to ICS-CERT 05/14/25 – ZDI asked for updates 05/14/25 - till 06/24/25, ICS-CERT tried to reach out to the vendor through different channels 06/24/25 – ZDI informed ICS-CERT of the intention to publish the case as a zero-day advisory -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product

## Disclosure Timeline

- 2025-03-05 - Vulnerability reported to vendor
- 2025-07-07 - Coordinated public release of advisory
- 2025-07-07 - Advisory Updated
