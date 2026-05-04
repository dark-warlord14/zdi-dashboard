# ZDI-25-409: RARLAB WinRAR Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-409
- **ZDI-CAN:** ZDI-CAN-27198
- **Date:** 2025-06-19
- **CVE:** CVE-2025-6218
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** RARLAB
- **Affected Products:** WinRAR
- **Credit:** whs3-detonator
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-409/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of RARLAB WinRAR. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of file paths within archive files. A crafted file path can cause the process to traverse to unintended directories. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

RARLAB has issued an update to correct this vulnerability. More details can be found at: https://www.win-rar.com/singlenewsview.html?&tx_ttnews%5Btt_news%5D=276&cHash=388885bd3908a40726f535c026f94eb6

## Disclosure Timeline

- 2025-06-05 - Vulnerability reported to vendor
- 2025-06-19 - Coordinated public release of advisory
- 2025-06-19 - Advisory Updated
