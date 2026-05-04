# ZDI-26-294: (0Day) Microsoft Windows library-ms NTLM Response Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-294
- **ZDI-CAN:** ZDI-CAN-28157
- **Date:** 2026-04-21
- **CVE:** N/A
- **CVSS:** 3.5
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** RootVector
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-294/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to disclose sensitive information on affected installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must view a folder containing malicious content. The specific flaw exists within the parsing of library-ms files. Crafted data in a library-ms file can trigger an outgoing WebDAV request. An attacker can leverage this vulnerability to disclose an NTLM response in the context of the current user.

## Additional Details

12/18/25 – ZDI reported the vulnerability to the vendor 12/18/25 – the vendor acknowledged the receipt of the report 03/04/26 – the vendor communicated that the vulnerability did not meet the bar for security servicing 04/13/26 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product

## Disclosure Timeline

- 2025-12-18 - Vulnerability reported to vendor
- 2026-04-21 - Coordinated public release of advisory
- 2026-04-21 - Advisory Updated
