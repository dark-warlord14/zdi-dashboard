# ZDI-21-998: Siemens Solid Edge Viewer DFT File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-998
- **ZDI-CAN:** ZDI-CAN-12993
- **Date:** 2021-08-24
- **CVE:** CVE-2021-31342
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Siemens
- **Affected Products:** Solid Edge Viewer
- **Credit:** garmin
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-998/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Siemens Solid Edge Viewer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of DFT files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Siemens has issued an update to correct this vulnerability. More details can be found at: https://cert-portal.siemens.com/productcert/pdf/ssa-208356.pdf

## Disclosure Timeline

- 2021-04-14 - Vulnerability reported to vendor
- 2021-08-24 - Coordinated public release of advisory
