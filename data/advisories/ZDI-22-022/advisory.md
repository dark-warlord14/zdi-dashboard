# ZDI-22-022: Siemens syngo fastView BMP File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-022
- **ZDI-CAN:** ZDI-CAN-14860
- **Date:** 2022-01-10
- **CVE:** CVE-2021-42028
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Siemens
- **Affected Products:** syngo fastView
- **Credit:** Tran Van Khang - khangkito (VinCSS)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-022/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Siemens syngo fastView. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of BMP images. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated structure. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

https://www.siemens-healthineers.com/support-documentation/cybersecurity/shsa-688797 https://www.cisa.gov/uscert/ics/advisories/icsa-21-350-16

## Disclosure Timeline

- 2021-10-15 - Vulnerability reported to vendor
- 2022-01-10 - Coordinated public release of advisory
