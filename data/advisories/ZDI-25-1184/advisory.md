# ZDI-25-1184: (0Day) FontForge GUtils BMP File Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1184
- **ZDI-CAN:** ZDI-CAN-27517
- **Date:** 2025-12-29
- **CVE:** CVE-2025-15279
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** FontForge
- **Affected Products:** FontForge
- **Credit:** volticks (@movx64 on twitter)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1184/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of FontForge. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of pixels within BMP files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

07/25/25 - ZDI submitted the reports to the vendor via a third-party platform 10/28/25 - ZDI asked for updates 12/04/25 – ZDI asked for updates 12/13/25 - ZDI reached out to the vendor’s GitHub account 12/13/25 – the vendor rejected the vulnerability, stating that only pull requests that include the required fixes will be considered 12/15/25 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory on 12/29/25 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product

## Disclosure Timeline

- 2025-07-23 - Vulnerability reported to vendor
- 2025-12-29 - Coordinated public release of advisory
- 2026-01-08 - Advisory Updated
