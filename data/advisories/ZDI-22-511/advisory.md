# ZDI-22-511: Siemens Simcenter Femap NEU File Parsing Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-511
- **ZDI-CAN:** ZDI-CAN-15048
- **Date:** 2022-03-18
- **CVE:** CVE-2021-46162
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Siemens
- **Affected Products:** Simcenter Femap
- **Credit:** xina1i
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-511/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Siemens Simcenter Femap. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of NEU files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated data structure. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

https://cert-portal.siemens.com/productcert/pdf/ssa-949188.pdf https://www.cisa.gov/uscert/ics/advisories/icsa-22-069-10

## Disclosure Timeline

- 2021-09-29 - Vulnerability reported to vendor
- 2022-03-18 - Coordinated public release of advisory
