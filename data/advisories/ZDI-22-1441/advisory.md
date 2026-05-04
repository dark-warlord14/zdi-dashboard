# ZDI-22-1441: Siemens Solid Edge Viewer DWG File Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1441
- **ZDI-CAN:** ZDI-CAN-17627
- **Date:** 2022-10-21
- **CVE:** CVE-2022-37864
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Siemens
- **Affected Products:** Solid Edge Viewer
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1441/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Siemens Solid Edge Viewer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of DWG files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

https://www.cisa.gov/uscert/ics/advisories/icsa-22-286-03 https://cert-portal.siemens.com/productcert/html/ssa-258115.html

## Disclosure Timeline

- 2022-06-22 - Vulnerability reported to vendor
- 2022-10-21 - Coordinated public release of advisory
