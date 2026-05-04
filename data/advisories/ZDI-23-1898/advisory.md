# ZDI-23-1898: Rockwell Automation Arena Simulation DOE File Parsing Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1898
- **ZDI-CAN:** ZDI-CAN-19750
- **Date:** 2023-12-21
- **CVE:** CVE-2023-29460
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Rockwell Automation
- **Affected Products:** Arena Simulation
- **Credit:** Simon Janz (@esj4y)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1898/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Rockwell Automation Arena Simulation. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of DOE files. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Rockwell Automation has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-23-131-10

## Disclosure Timeline

- 2023-02-24 - Vulnerability reported to vendor
- 2023-12-21 - Coordinated public release of advisory
