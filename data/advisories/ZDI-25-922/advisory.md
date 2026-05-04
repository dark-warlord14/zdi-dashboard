# ZDI-25-922: Ivanti Endpoint Manager EFile Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-922
- **ZDI-CAN:** ZDI-CAN-26833
- **Date:** 2025-09-30
- **CVE:** CVE-2025-9712
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Ivanti
- **Affected Products:** Endpoint Manager
- **Credit:** 06fe5fd2bc53027c4a3b7e395af0b850e7b8a044
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-922/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Ivanti Endpoint Manager. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. Alternatively, no user interaction is required if the attacker has administrative credentials to the application. The specific flaw exists within the EFile class. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

Ivanti has issued an update to correct this vulnerability. More details can be found at: https://forums.ivanti.com/s/article/Security-Advisory-September-2025-for-Ivanti-EPM-2024-SU3-and-EPM-2022-SU8?language=en_US

## Disclosure Timeline

- 2025-05-29 - Vulnerability reported to vendor
- 2025-09-30 - Coordinated public release of advisory
- 2025-09-30 - Advisory Updated
