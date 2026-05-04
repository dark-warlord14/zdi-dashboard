# ZDI-24-1653: Rockwell Automation Arena Simulation DOE File Parsing Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1653
- **ZDI-CAN:** ZDI-CAN-24544
- **Date:** 2024-12-10
- **CVE:** CVE-2024-11155
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Rockwell Automation
- **Affected Products:** Arena Simulation
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1653/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Rockwell Automation Arena Simulation. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of DOE files. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Rockwell Automation has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-24-345-06

## Disclosure Timeline

- 2024-06-13 - Vulnerability reported to vendor
- 2024-12-10 - Coordinated public release of advisory
- 2024-12-10 - Advisory Updated
