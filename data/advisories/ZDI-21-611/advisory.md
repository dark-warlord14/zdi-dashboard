# ZDI-21-611: Siemens Solid Edge Viewer PAR File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-611
- **ZDI-CAN:** ZDI-CAN-12529
- **Date:** 2021-05-25
- **CVE:** CVE-2021-25678
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Siemens
- **Affected Products:** Solid Edge Viewer
- **Credit:** Francis Provencher {PRL}
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-611/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Siemens Solid Edge Viewer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of PAR files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

https://cert-portal.siemens.com/productcert/pdf/ssa-574442.pdf https://us-cert.cisa.gov/ics/advisories/icsa-21-103-06

## Disclosure Timeline

- 2021-01-13 - Vulnerability reported to vendor
- 2021-05-25 - Coordinated public release of advisory
- 2021-05-25 - Advisory Updated
