# ZDI-25-935: (0Day) Ivanti Endpoint Manager OnSaveToDB Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-935
- **ZDI-CAN:** ZDI-CAN-26834
- **Date:** 2025-10-16
- **CVE:** CVE-2025-9713
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Ivanti
- **Affected Products:** Endpoint Manager
- **Credit:** 06fe5fd2bc53027c4a3b7e395af0b850e7b8a044
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-935/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Ivanti Endpoint Manager. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. Alternatively, no user interaction is required if the attacker has administrative credentials to the application. The specific flaw exists within the implementation of the OnSaveToDB method. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

06/03/25 – ZDI reported the vulnerability to the vendor 06/04/25 – the vendor acknowledged the receipt of the report 07/24/25 – the vendor communicated that the issue would be patched in September 2025 07/29/25 - the vendor requested an extension until March 2026 09/26/25 - ZDI notified the vendor of the intention to publish case as a 0-day advisory 10/13/2025 - the vendor published a security advisory -- Mitigation: On 11/12/2025 the vendor published a fix for the vulnerability: https://forums.ivanti.com/s/article/Security-Advisory-EPM-November-2025-for-EPM-2024?language=en_US

## Disclosure Timeline

- 2025-06-03 - Vulnerability reported to vendor
- 2025-10-16 - Coordinated public release of advisory
- 2025-11-17 - Advisory Updated
