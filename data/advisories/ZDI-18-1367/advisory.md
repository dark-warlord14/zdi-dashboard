# ZDI-18-1367: OMRON CX-One CX-Programmer CXP File Parsing Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1367
- **ZDI-CAN:** ZDI-CAN-6608
- **Date:** 2018-12-10
- **CVE:** CVE-2018-18989
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Omron
- **Affected Products:** CX-One
- **Credit:** Esteban Ruiz (mr_me) of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1367/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of OMRON CX-One CX-Programmer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Omron has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-18-338-01

## Disclosure Timeline

- 2018-07-05 - Vulnerability reported to vendor
- 2018-12-10 - Coordinated public release of advisory
