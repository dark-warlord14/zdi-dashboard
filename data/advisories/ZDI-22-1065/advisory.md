# ZDI-22-1065: Apple macOS Remote Events Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1065
- **ZDI-CAN:** ZDI-CAN-15191
- **Date:** 2022-08-15
- **CVE:** CVE-2022-22630
- **CVSS:** 8.1
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Jeremy Brown
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1065/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Apple macOS. Authentication is not required to exploit this vulnerability. The specific flaw exists within Apple Remote Events. The issue results from the lack of proper validation of user-supplied data, which can result in a memory corruption condition. An attacker can leverage this vulnerability to execute code in the context of the AEServer process.

## Additional Details

ZDI-CAN-15191 / CVE-2022-22630 was addressed in macOS Monterey 12.3.

## Disclosure Timeline

- 2021-12-22 - Vulnerability reported to vendor
- 2022-08-15 - Coordinated public release of advisory
