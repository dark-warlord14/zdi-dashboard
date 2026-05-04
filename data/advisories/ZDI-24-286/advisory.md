# ZDI-24-286: NI LabVIEW VI File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-286
- **ZDI-CAN:** ZDI-CAN-21984
- **Date:** 2024-03-12
- **CVE:** CVE-2024-23608
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** NI
- **Affected Products:** LabVIEW
- **Credit:** 06fe5fd2bc53027c4a3b7e395af0b850e7b8a044
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-286/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of NI LabVIEW. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of VI files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

NI has issued an update to correct this vulnerability. More details can be found at: https://www.ni.com/en/support/security/available-critical-and-security-updates-for-ni-software/out-of-bounds-write-due-to-missing-bounds-check-in-labview.html

## Disclosure Timeline

- 2023-12-01 - Vulnerability reported to vendor
- 2024-03-12 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
