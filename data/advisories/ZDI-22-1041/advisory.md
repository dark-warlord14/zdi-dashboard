# ZDI-22-1041: (Pwn2Own) ICONICS GENESIS64 genbroker64 Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1041
- **ZDI-CAN:** ZDI-CAN-17200
- **Date:** 2022-08-03
- **CVE:** CVE-2022-33318
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** ICONICS
- **Affected Products:** GENESIS64
- **Credit:** Axel '0vercl0k' Souchet
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1041/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of ICONICS GENESIS64. Authentication is not required to exploit this vulnerability. The specific flaw exists within the GenBroker64 service. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the Administrator.

## Additional Details

ICONICS has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/uscert/ics/advisories/icsa-22-202-04

## Disclosure Timeline

- 2022-05-09 - Vulnerability reported to vendor
- 2022-08-03 - Coordinated public release of advisory
