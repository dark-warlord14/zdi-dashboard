# ZDI-21-1122: Siemens Solid Edge Viewer OBJ File Parsing Uninitialized Pointer Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1122
- **ZDI-CAN:** ZDI-CAN-13770
- **Date:** 2021-09-30
- **CVE:** CVE-2021-41538
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Siemens
- **Affected Products:** Solid Edge Viewer
- **Credit:** xina1i
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1122/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Siemens Solid Edge Viewer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of OBJ files. The issue results from the lack of proper initialization of a pointer prior to accessing it. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

https://www.siemens.com/cert/advisories/ https://cert-portal.siemens.com/productcert/pdf/ssa-728618.pdf

## Disclosure Timeline

- 2021-05-19 - Vulnerability reported to vendor
- 2021-09-30 - Coordinated public release of advisory
