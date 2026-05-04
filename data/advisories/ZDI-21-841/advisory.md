# ZDI-21-841: Siemens JT2Go TIF File Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-841
- **ZDI-CAN:** ZDI-CAN-13353
- **Date:** 2021-07-19
- **CVE:** CVE-2021-34312
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Siemens
- **Affected Products:** JT2Go
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-841/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Siemens JT2Go. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of TIF files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

https://us-cert.cisa.gov/ics/advisories/icsa-21-194-15 https://cert-portal.siemens.com/productcert/pdf/ssa-483182.pdf

## Disclosure Timeline

- 2021-03-10 - Vulnerability reported to vendor
- 2021-07-19 - Coordinated public release of advisory
