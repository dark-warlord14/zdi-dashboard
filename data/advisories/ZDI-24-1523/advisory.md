# ZDI-24-1523: Siemens Tecnomatix Plant Simulation WRL File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1523
- **ZDI-CAN:** ZDI-CAN-24231
- **Date:** 2024-11-19
- **CVE:** CVE-2024-52565
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Siemens
- **Affected Products:** Tecnomatix Plant Simulation
- **Credit:** Rocco Calvi (@TecR0c) with TecSecurity
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1523/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Siemens Tecnomatix Plant Simulation. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of WRL files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Siemens has issued an update to correct this vulnerability. More details can be found at: https://cert-portal.siemens.com/productcert/html/ssa-824503.html

## Disclosure Timeline

- 2024-06-13 - Vulnerability reported to vendor
- 2024-11-19 - Coordinated public release of advisory
- 2024-11-19 - Advisory Updated
