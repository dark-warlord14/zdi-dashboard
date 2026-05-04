# ZDI-22-1440: Siemens Simcenter Femap JT File Parsing Uninitialized Pointer Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1440
- **ZDI-CAN:** ZDI-CAN-16973
- **Date:** 2022-10-17
- **CVE:** CVE-2022-41851
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Siemens
- **Affected Products:** Simcenter Femap
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1440/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Siemens Simcenter Femap. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of JT files. The issue results from the lack of proper initialization of a pointer prior to accessing it. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

https://cert-portal.siemens.com/productcert/html/ssa-611756.html https://www.cisa.gov/uscert/ics/advisories/icsa-22-286-10

## Disclosure Timeline

- 2022-04-27 - Vulnerability reported to vendor
- 2022-10-17 - Coordinated public release of advisory
