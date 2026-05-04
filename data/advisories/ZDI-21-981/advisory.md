# ZDI-21-981: Siemens JT2Go PAR File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-981
- **ZDI-CAN:** ZDI-CAN-13405
- **Date:** 2021-08-18
- **CVE:** CVE-2021-33738
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Siemens
- **Affected Products:** JT2Go
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-981/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Siemens JT2Go. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of PAR files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

https://us-cert.cisa.gov/ics/advisories/icsa-21-222-03 https://cert-portal.siemens.com/productcert/pdf/ssa-938030.pdf

## Disclosure Timeline

- 2021-03-16 - Vulnerability reported to vendor
- 2021-08-18 - Coordinated public release of advisory
