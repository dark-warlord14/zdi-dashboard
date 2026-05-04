# ZDI-22-008: Siemens JT2Go JT File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-008
- **ZDI-CAN:** ZDI-CAN-15102
- **Date:** 2022-01-06
- **CVE:** CVE-2021-44012
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Siemens
- **Affected Products:** JT2Go
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-008/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Siemens JT2Go. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of JT files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

https://cert-portal.siemens.com/productcert/pdf/ssa-595101.pdf https://www.cisa.gov/uscert/ics/advisories/icsa-21-350-10

## Disclosure Timeline

- 2021-08-27 - Vulnerability reported to vendor
- 2022-01-06 - Coordinated public release of advisory
- 2022-01-09 - Advisory Updated
