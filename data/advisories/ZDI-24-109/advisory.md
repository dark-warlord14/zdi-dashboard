# ZDI-24-109: Allegra uploadSimpleFile Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-109
- **ZDI-CAN:** ZDI-CAN-22527
- **Date:** 2024-02-09
- **CVE:** CVE-2023-51646
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Allegra
- **Affected Products:** Allegra
- **Credit:** 06fe5fd2bc53027c4a3b7e395af0b850e7b8a044
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-109/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Allegra. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the uploadSimpleFile method. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of LOCAL SERVICE.

## Additional Details

Allegra has issued an update to correct this vulnerability. More details can be found at: https://www.trackplus.com/en/service/release-notes-reader/7-5-1-release-notes-2.html

## Disclosure Timeline

- 2023-12-06 - Vulnerability reported to vendor
- 2024-02-09 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
