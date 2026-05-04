# ZDI-24-476: (Pwn2Own) QNAP TS-464 HLS_tmp Directory Traversal Arbitrary File Creation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-476
- **ZDI-CAN:** ZDI-CAN-22407
- **Date:** 2024-05-19
- **CVE:** CVE-2023-51365
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L/A:H
- **Affected Vendors:** QNAP
- **Affected Products:** TS-464
- **Credit:** Thalium team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-476/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of QNAP TS-464 NAS devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of the HLS_tmp parameter provided to the share.cgi endpoint. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to create or modify files in the context of admin.

## Additional Details

QNAP has issued an update to correct this vulnerability. More details can be found at: https://www.qnap.com/en/security-advisory/qsa-24-14

## Disclosure Timeline

- 2023-11-09 - Vulnerability reported to vendor
- 2024-05-19 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
