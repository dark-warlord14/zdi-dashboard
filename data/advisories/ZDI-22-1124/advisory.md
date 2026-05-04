# ZDI-22-1124: (Pwn2Own) AVEVA Edge SetBytesToManagedControl Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1124
- **ZDI-CAN:** ZDI-CAN-17212
- **Date:** 2022-08-23
- **CVE:** CVE-2022-28685
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** AVEVA
- **Affected Products:** Edge
- **Credit:** Chris Anastasio (muffin) and Steven Seeley (mr_me) of Incite Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1124/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of AVEVA Edge. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of APP files. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

AVEVA has issued an update to correct this vulnerability. More details can be found at: https://www.aveva.com/content/dam/aveva/documents/support/cyber-security-updates/SecurityBulletin_AVEVA-2022-005.pdf

## Disclosure Timeline

- 2022-05-09 - Vulnerability reported to vendor
- 2022-08-23 - Coordinated public release of advisory
