# ZDI-21-990: Siemens JT2Go DGN File Parsing Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-990
- **ZDI-CAN:** ZDI-CAN-13468
- **Date:** 2021-08-18
- **CVE:** CVE-2021-32944
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Siemens
- **Affected Products:** JT2Go
- **Credit:** Brian Gorenc of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-990/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Siemens JT2Go. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of DGN files. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

https://us-cert.cisa.gov/ics/advisories/icsa-21-222-01 https://cert-portal.siemens.com/productcert/pdf/ssa-365397.pdf

## Disclosure Timeline

- 2021-03-18 - Vulnerability reported to vendor
- 2021-08-18 - Coordinated public release of advisory
