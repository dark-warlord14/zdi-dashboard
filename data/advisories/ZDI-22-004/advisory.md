# ZDI-22-004: Siemens JT2Go PDF File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-004
- **ZDI-CAN:** ZDI-CAN-14974
- **Date:** 2022-01-06
- **CVE:** CVE-2021-44001
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Siemens
- **Affected Products:** JT2Go
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-004/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Siemens JT2Go. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of PDF files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

https://cert-portal.siemens.com/productcert/pdf/ssa-595101.pdf https://www.cisa.gov/uscert/ics/advisories/icsa-21-350-10

## Disclosure Timeline

- 2021-08-20 - Vulnerability reported to vendor
- 2022-01-06 - Coordinated public release of advisory
- 2022-01-09 - Advisory Updated
