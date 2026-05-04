# ZDI-21-983: Siemens JT2Go DGN File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-983
- **ZDI-CAN:** ZDI-CAN-13409
- **Date:** 2021-08-18
- **CVE:** CVE-2021-32946
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Siemens
- **Affected Products:** JT2Go
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-983/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Siemens JT2Go. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of DGN files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

https://us-cert.cisa.gov/ics/advisories/icsa-21-222-03 https://cert-portal.siemens.com/productcert/pdf/ssa-938030.pdf

## Disclosure Timeline

- 2021-03-16 - Vulnerability reported to vendor
- 2021-08-18 - Coordinated public release of advisory
