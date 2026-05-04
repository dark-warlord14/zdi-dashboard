# ZDI-19-993: Rockwell Automation Arena Simulation DOE File Parsing Uninitialized Pointer Dereference Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-993
- **ZDI-CAN:** ZDI-CAN-8682
- **Date:** 2019-11-26
- **CVE:** CVE-2019-13527
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Rockwell Automation
- **Affected Products:** Arena Simulation
- **Credit:** kimiya of 9SG Security Team - kimiya@9sgsec.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-993/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Rockwell Automation Arena Simulation. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of DOE files. The issue results from the lack of proper initialization of a pointer prior to accessing it. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Rockwell Automation has issued an update to correct this vulnerability. More details can be found at: https://www.us-cert.gov/ics/advisories/icsa-19-213-05

## Disclosure Timeline

- 2019-07-11 - Vulnerability reported to vendor
- 2019-11-26 - Coordinated public release of advisory
