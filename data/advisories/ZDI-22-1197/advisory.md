# ZDI-22-1197: (0Day) Ansys SpaceClaim X_B File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1197
- **ZDI-CAN:** ZDI-CAN-17317
- **Date:** 2022-09-14
- **CVE:** CVE-2022-40641
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Ansys
- **Affected Products:** SpaceClaim
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1197/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Ansys SpaceClaim. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of X_B files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated data structure. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fixed in Ansys SpaceClaim 2023 R2.

## Disclosure Timeline

- 2022-07-19 - Vulnerability reported to vendor
- 2022-09-14 - Coordinated public release of advisory
- 2023-09-07 - Advisory Updated
