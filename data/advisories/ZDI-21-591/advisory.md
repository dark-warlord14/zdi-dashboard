# ZDI-21-591: QNAP NAS MusicStation Directory Traversal Arbitrary File Creation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-591
- **ZDI-CAN:** ZDI-CAN-12048
- **Date:** 2021-05-14
- **CVE:** CVE-2020-36197
- **CVSS:** 7.1
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:H
- **Affected Vendors:** QNAP
- **Affected Products:** NAS
- **Credit:** polict of Shielder
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-591/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to create arbitrary files on affected installations of QNAP NAS. Authentication is not required to exploit this vulnerability. The specific flaw exists within the MusicStation application. When parsing the arttype request parameter, the process does not properly validate a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to create files in the context of the admin user.

## Additional Details

QNAP has issued an update to correct this vulnerability. More details can be found at: https://www.qnap.com/zh-tw/security-advisory/qsa-21-08

## Disclosure Timeline

- 2021-01-20 - Vulnerability reported to vendor
- 2021-05-14 - Coordinated public release of advisory
