# ZDI-21-228: Siemens JT2Go PAR File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-228
- **ZDI-CAN:** ZDI-CAN-12043
- **Date:** 2021-02-24
- **CVE:** CVE-2020-27002
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Siemens
- **Affected Products:** JT2Go
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-228/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Siemens JT2Go. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of PAR files. The issue results from the lack of proper validation of user-supplied data, which can result in a read before the start of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

https://cert-portal.siemens.com/productcert/pdf/ssa-695540.pdf https://us-cert.cisa.gov/ics/advisories/icsa-21-147-04

## Disclosure Timeline

- 2020-12-02 - Vulnerability reported to vendor
- 2021-02-24 - Coordinated public release of advisory
- 2021-06-08 - Advisory Updated
