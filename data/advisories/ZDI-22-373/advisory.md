# ZDI-22-373: Omron CX-One SDD File Parsing Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-373
- **ZDI-CAN:** ZDI-CAN-14038
- **Date:** 2022-02-16
- **CVE:** CVE-2022-21137
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Omron
- **Affected Products:** CX-One
- **Credit:** xina1i
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-373/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Omron CX-One. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of SDD files in the CXDrive module. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Omron has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/uscert/ics/advisories/icsa-22-006-01

## Disclosure Timeline

- 2021-07-20 - Vulnerability reported to vendor
- 2022-02-16 - Coordinated public release of advisory
