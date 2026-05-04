# ZDI-18-1351: OMRON CX-Supervisor SCS File Parsing Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1351
- **ZDI-CAN:** ZDI-CAN-6663
- **Date:** 2018-11-21
- **CVE:** CVE-2018-7521
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Omron
- **Affected Products:** CX-Supervisor
- **Credit:** Esteban Ruiz (mr_me) of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1351/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of OMRON CX-Supervisor. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of project files. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Omron has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-18-072-01

## Disclosure Timeline

- 2018-07-09 - Vulnerability reported to vendor
- 2018-11-21 - Coordinated public release of advisory
