# ZDI-25-837: Rockwell Automation Arena Simulation DOE File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-837
- **ZDI-CAN:** ZDI-CAN-26559
- **Date:** 2025-08-13
- **CVE:** CVE-2025-6377
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Rockwell Automation
- **Affected Products:** Arena Simulation
- **Credit:** Simon (@esj4y) Janz
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-837/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Rockwell Automation Arena Simulation. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of DOE files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Rockwell Automation has issued an update to correct this vulnerability. More details can be found at: https://www.rockwellautomation.com/en-us/trust-center/security-advisories/advisory.SD1729.html

## Disclosure Timeline

- 2025-03-11 - Vulnerability reported to vendor
- 2025-08-13 - Coordinated public release of advisory
- 2025-08-13 - Advisory Updated
