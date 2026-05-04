# ZDI-25-1101: Fuji Electric Monitouch V-SFT V7 File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1101
- **ZDI-CAN:** ZDI-CAN-27438
- **Date:** 2025-12-17
- **CVE:** CVE-2025-53524
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Fuji Electric
- **Affected Products:** Monitouch V-SFT
- **Credit:** Rocco Calvi (@TecR0c) with TecSecurity
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1101/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Fuji Electric Monitouch V-SFT. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of V7 files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fuji Electric has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-25-308-01

## Disclosure Timeline

- 2025-07-22 - Vulnerability reported to vendor
- 2025-12-17 - Coordinated public release of advisory
- 2025-12-17 - Advisory Updated
