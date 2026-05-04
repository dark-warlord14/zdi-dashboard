# ZDI-22-1039: (Pwn2Own) ICONICS GENESIS64 TDFX File Parsing Exposed Dangerous Function Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1039
- **ZDI-CAN:** ZDI-CAN-17198
- **Date:** 2022-08-03
- **CVE:** CVE-2022-33317
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** ICONICS
- **Affected Products:** GENESIS64
- **Credit:** Ben McBride
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1039/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of ICONICS GENESIS64. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of TDFX files. The issue results from the exposure of a dangerous method. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

ICONICS has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/uscert/ics/advisories/icsa-22-202-04

## Disclosure Timeline

- 2022-05-09 - Vulnerability reported to vendor
- 2022-08-03 - Coordinated public release of advisory
