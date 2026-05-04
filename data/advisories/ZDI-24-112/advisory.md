# ZDI-24-112: Allegra downloadAttachmentGlobal Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-112
- **ZDI-CAN:** ZDI-CAN-22507
- **Date:** 2024-02-09
- **CVE:** CVE-2023-52334
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Allegra
- **Affected Products:** Allegra
- **Credit:** 06fe5fd2bc53027c4a3b7e395af0b850e7b8a044
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-112/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Allegra. Although authentication is required to exploit this vulnerability, product implements a registration mechanism that can be used to create a user with a sufficient privilege level. The specific flaw exists within the downloadAttachmentGlobal action. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

Allegra has issued an update to correct this vulnerability. More details can be found at: https://www.trackplus.com/en/service/release-notes-reader/7-5-1-release-notes-2.html

## Disclosure Timeline

- 2023-12-08 - Vulnerability reported to vendor
- 2024-02-09 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
