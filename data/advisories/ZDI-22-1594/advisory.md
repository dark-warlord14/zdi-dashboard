# ZDI-22-1594: Siemens Simcenter Femap X_T File Parsing Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1594
- **ZDI-CAN:** ZDI-CAN-17745
- **Date:** 2022-11-17
- **CVE:** CVE-2022-39157
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Siemens
- **Affected Products:** Simcenter Femap
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1594/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Siemens Simcenter Femap. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of X_T files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated data structure. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

https://www.cisa.gov/uscert/ics/advisories/icsa-22-314-01 https://cert-portal.siemens.com/productcert/html/ssa-853037.html

## Disclosure Timeline

- 2022-07-28 - Vulnerability reported to vendor
- 2022-11-17 - Coordinated public release of advisory
