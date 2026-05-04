# ZDI-24-1501: Ivanti Endpoint Manager EFile Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1501
- **ZDI-CAN:** ZDI-CAN-24272
- **Date:** 2024-11-13
- **CVE:** CVE-2024-34787
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Ivanti
- **Affected Products:** Endpoint Manager
- **Credit:** 06fe5fd2bc53027c4a3b7e395af0b850e7b8a044
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1501/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Ivanti Endpoint Manager. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. Alternatively, no user interaction is required if the attacker has administrative credentials to the application. The specific flaw exists within the EFile class. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

Ivanti has issued an update to correct this vulnerability. More details can be found at: https://forums.ivanti.com/s/article/Security-Advisory-EPM-November-2024-for-EPM-2024-and-EPM-2022

## Disclosure Timeline

- 2024-06-06 - Vulnerability reported to vendor
- 2024-11-13 - Coordinated public release of advisory
- 2024-11-13 - Advisory Updated
