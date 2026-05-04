# ZDI-24-271: Dassault Systèmes eDrawings SAT File Parsing Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-271
- **ZDI-CAN:** ZDI-CAN-22846
- **Date:** 2024-03-11
- **CVE:** CVE-2024-1847
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Dassault Systèmes
- **Affected Products:** eDrawings
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-271/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Dassault Syst��mes eDrawings. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of SAT files. The issue results from the lack of proper validation of user-supplied data, which can result in a memory corruption condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Dassault Systèmes has issued an update to correct this vulnerability. More details can be found at: https://www.3ds.com/vulnerability/advisories

## Disclosure Timeline

- 2023-12-15 - Vulnerability reported to vendor
- 2024-03-11 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
