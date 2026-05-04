# ZDI-21-781: Siemens Simcenter Femap modfem File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-781
- **ZDI-CAN:** ZDI-CAN-12820
- **Date:** 2021-07-07
- **CVE:** CVE-2021-27399
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Siemens
- **Affected Products:** Simcenter Femap
- **Credit:** Francis Provencher {PRL}
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-781/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Siemens Simcenter Femap. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of modfem files. The issue results from the lack of proper validation of user-supplied data, which can result in a write before the start of an allocated data structure. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

https://us-cert.cisa.gov/ics/advisories/icsa-21-159-12 https://cert-portal.siemens.com/productcert/pdf/ssa-133038.pdf

## Disclosure Timeline

- 2021-03-05 - Vulnerability reported to vendor
- 2021-07-07 - Coordinated public release of advisory
