# ZDI-22-295: Siemens Simcenter Femap NEU File Parsing Uninitialized Pointer Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-295
- **ZDI-CAN:** ZDI-CAN-14755
- **Date:** 2022-02-11
- **CVE:** CVE-2021-46152
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Siemens
- **Affected Products:** Simcenter Femap
- **Credit:** xina1i
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-295/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Siemens Simcenter Femap. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of NEU files. The issue results from the lack of proper initialization of a pointer prior to accessing it. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Siemens has issued an update to correct this vulnerability. More details can be found at: https://cert-portal.siemens.com/productcert/pdf/ssa-609880.pdf

## Disclosure Timeline

- 2021-09-29 - Vulnerability reported to vendor
- 2022-02-11 - Coordinated public release of advisory
