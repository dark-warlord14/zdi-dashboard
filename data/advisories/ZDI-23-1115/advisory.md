# ZDI-23-1115: Siemens Solid Edge Viewer DWG File Parsing Use-After-Free Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1115
- **ZDI-CAN:** ZDI-CAN-19562
- **Date:** 2023-08-15
- **CVE:** CVE-2023-39549
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Siemens
- **Affected Products:** Solid Edge Viewer
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1115/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Siemens Solid Edge Viewer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of DWG files. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Siemens has issued an update to correct this vulnerability. More details can be found at: https://cert-portal.siemens.com/productcert/html/ssa-932528.html

## Disclosure Timeline

- 2022-11-21 - Vulnerability reported to vendor
- 2023-08-15 - Coordinated public release of advisory
