# ZDI-25-1086: (0Day) Soda PDF Desktop CBZ File Parsing Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1086
- **ZDI-CAN:** ZDI-CAN-27509
- **Date:** 2025-12-11
- **CVE:** CVE-2025-14413
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Soda PDF
- **Affected Products:** Desktop
- **Credit:** kimiya
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1086/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Soda PDF Desktop. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of CBZ files. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

08/26/25 - ZDI reported the vulnerability to Avanquest’s support team 09/11/25 - ZDI asked for updates 11/12/25 - ZDI asked for updates 11/21/25 – the vendor indicated that they don't offer bounties or rewards 11/21/25 - ZDI confirmed not accepting any rewards or bounties and asked for the expected fix date 12/04/25 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory on 12/11/25 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product

## Disclosure Timeline

- 2025-08-26 - Vulnerability reported to vendor
- 2025-12-11 - Coordinated public release of advisory
- 2025-12-11 - Advisory Updated
