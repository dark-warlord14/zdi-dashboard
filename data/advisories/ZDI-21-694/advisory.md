# ZDI-21-694: Siemens JT2Go TIFF File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-694
- **ZDI-CAN:** ZDI-CAN-13131
- **Date:** 2021-06-17
- **CVE:** CVE-2021-27390
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Siemens
- **Affected Products:** JT2Go
- **Credit:** xina1i at SecZone
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-694/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Siemens JT2Go. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of TIFF files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

https://nvd.nist.gov/vuln/detail/CVE-2021-27390 https://cert-portal.siemens.com/productcert/pdf/ssa-645530.pdf

## Disclosure Timeline

- 2021-02-17 - Vulnerability reported to vendor
- 2021-06-17 - Coordinated public release of advisory
