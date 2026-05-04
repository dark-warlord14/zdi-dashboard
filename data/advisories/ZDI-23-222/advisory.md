# ZDI-23-222: Omron CX-One CXP File Parsing Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-222
- **ZDI-CAN:** ZDI-CAN-15352
- **Date:** 2023-03-07
- **CVE:** CVE-2022-3398
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Omron
- **Affected Products:** CX-One
- **Credit:** xina1i
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-222/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Omron CX-One. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of CXP files in the CX-Position module. The issue results from the lack of proper validation of user-supplied data, which can result in a memory corruption condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Omron has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-22-277-04

## Disclosure Timeline

- 2022-06-01 - Vulnerability reported to vendor
- 2023-03-07 - Coordinated public release of advisory
