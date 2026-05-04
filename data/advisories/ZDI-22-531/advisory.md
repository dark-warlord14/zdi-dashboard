# ZDI-22-531: Siemens syngo fastView BMP File Parsing Write-what-where Condition Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-531
- **ZDI-CAN:** ZDI-CAN-15696
- **Date:** 2022-03-23
- **CVE:** CVE-2021-45465
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Siemens
- **Affected Products:** syngo fastView
- **Credit:** Tran Van Khang - khangkito (VinCSS)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-531/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Siemens syngo fastView. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of BMP files. The issue results from the lack of proper validation of user-supplied data, which can result in a write-what-where condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

https://www.cisa.gov/uscert/ics/advisories/icsa-21-350-16 https://www.siemens-healthineers.com/support-documentation/cybersecurity/shsa-688797

## Disclosure Timeline

- 2021-12-16 - Vulnerability reported to vendor
- 2022-03-23 - Coordinated public release of advisory
