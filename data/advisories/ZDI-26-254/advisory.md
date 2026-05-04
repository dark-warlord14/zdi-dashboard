# ZDI-26-254: (0Day) Labcenter Electronics Proteus PDSPRJ File Parsing Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-254
- **ZDI-CAN:** ZDI-CAN-25717
- **Date:** 2026-04-06
- **CVE:** CVE-2026-5496
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Labcenter Electronics
- **Affected Products:** Proteus
- **Credit:** Andrea Micalizzi aka rgod (@rgod777)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-254/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Labcenter Electronics Proteus. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of PDSPRJ files. The issue results from the lack of proper validation of user-supplied data, which can result in a type confusion condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

04/14/25 - ZDI submitted the report to the vendor 10/10/25 – ZDI asked for updates 10/16/25 – the vendor communicated that the software and installer were no longer in production 11/06/25 – ZDI requested the product's EoL announcement 11/28/25 – ZDI notified the vendor of the intention to publish the case as a zero-day advisory -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product

## Disclosure Timeline

- 2025-04-14 - Vulnerability reported to vendor
- 2026-04-06 - Coordinated public release of advisory
- 2026-04-21 - Advisory Updated
