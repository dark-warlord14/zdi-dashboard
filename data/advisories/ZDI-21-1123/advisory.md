# ZDI-21-1123: Siemens Solid Edge Viewer OBJ File Parsing Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1123
- **ZDI-CAN:** ZDI-CAN-13773
- **Date:** 2021-09-30
- **CVE:** CVE-2021-41539
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Siemens
- **Affected Products:** Solid Edge Viewer
- **Credit:** xina1i
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1123/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Siemens Solid Edge Viewer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of OBJ files. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

https://www.siemens.com/cert/advisories/ https://cert-portal.siemens.com/productcert/pdf/ssa-728618.pdf

## Disclosure Timeline

- 2021-05-19 - Vulnerability reported to vendor
- 2021-09-30 - Coordinated public release of advisory
