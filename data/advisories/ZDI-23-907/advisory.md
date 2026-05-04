# ZDI-23-907: Siemens Solid Edge Viewer DWG File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-907
- **ZDI-CAN:** ZDI-CAN-19432
- **Date:** 2023-07-10
- **CVE:** CVE-2023-26495
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Siemens
- **Affected Products:** Solid Edge Viewer
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-907/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Siemens Solid Edge Viewer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of DWG files. Crafted data in a DWG file can trigger a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

https://www.opendesign.com/security-advisories https://cert-portal.siemens.com/productcert/html/ssa-975766.html

## Disclosure Timeline

- 2022-11-11 - Vulnerability reported to vendor
- 2023-07-10 - Coordinated public release of advisory
