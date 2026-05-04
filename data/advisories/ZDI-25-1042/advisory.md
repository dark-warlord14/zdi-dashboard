# ZDI-25-1042: Siemens Simcenter Femap IGS File Parsing Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1042
- **ZDI-CAN:** ZDI-CAN-26755
- **Date:** 2025-12-09
- **CVE:** CVE-2025-40936
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Siemens
- **Affected Products:** Simcenter Femap
- **Credit:** Rocco Calvi (@TecR0c) with TecSecurity
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1042/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Siemens Simcenter Femap. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of IGS files. The issue results from the lack of proper validation of user-supplied data, which can result in a read before the start of an allocated array. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Siemens has issued an update to correct this vulnerability. More details can be found at: https://cert-portal.siemens.com/productcert/html/ssa-241605.html

## Disclosure Timeline

- 2025-04-25 - Vulnerability reported to vendor
- 2025-12-09 - Coordinated public release of advisory
- 2025-12-09 - Advisory Updated
