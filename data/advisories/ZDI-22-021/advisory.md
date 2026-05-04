# ZDI-22-021: Siemens syngo DCM File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-021
- **ZDI-CAN:** ZDI-CAN-15097
- **Date:** 2022-01-10
- **CVE:** CVE-2021-40367
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Siemens
- **Affected Products:** syngo fastView
- **Credit:** Tran Van Khang - khangkito (VinCSS)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-021/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Siemens syngo. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of DCM files. Crafted data in a DCM file can trigger a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

https://www.siemens-healthineers.com/support-documentation/cybersecurity/shsa-688797 https://www.cisa.gov/uscert/ics/advisories/icsa-21-350-16

## Disclosure Timeline

- 2021-09-01 - Vulnerability reported to vendor
- 2022-01-10 - Coordinated public release of advisory
