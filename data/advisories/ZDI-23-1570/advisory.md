# ZDI-23-1570: Siemens Tecnomatix Plant Simulation SPP File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1570
- **ZDI-CAN:** ZDI-CAN-21132
- **Date:** 2023-10-19
- **CVE:** CVE-2023-38680
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Siemens
- **Affected Products:** Tecnomatix Plant Simulation
- **Credit:** Simon Janz (@esj4y)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1570/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Siemens Tecnomatix Plant Simulation. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of SPP files. The issue results from the lack of proper validation of user-supplied data, which can result in a write before the start of an allocated data structure. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Siemens has issued an update to correct this vulnerability. More details can be found at: https://cert-portal.siemens.com/productcert/html/ssa-764801.html

## Disclosure Timeline

- 2023-05-19 - Vulnerability reported to vendor
- 2023-10-19 - Coordinated public release of advisory
