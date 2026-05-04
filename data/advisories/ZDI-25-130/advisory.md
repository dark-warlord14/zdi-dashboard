# ZDI-25-130: Siemens Simcenter Femap NEU File Parsing Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-130
- **ZDI-CAN:** ZDI-CAN-25443
- **Date:** 2025-03-13
- **CVE:** CVE-2025-25175
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Siemens
- **Affected Products:** Simcenter Femap
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-130/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Siemens Simcenter Femap. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of NEU files. The issue results from the lack of proper validation of user-supplied data, which can result in a memory corruption condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Siemens has issued an update to correct this vulnerability. More details can be found at: https://cert-portal.siemens.com/productcert/html/ssa-920092.html

## Disclosure Timeline

- 2024-11-13 - Vulnerability reported to vendor
- 2025-03-13 - Coordinated public release of advisory
- 2025-03-13 - Advisory Updated
