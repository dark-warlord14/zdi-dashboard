# ZDI-21-216: Mozilla Firefox WebGL2 compressedTexImage3D Handling Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-216
- **ZDI-CAN:** ZDI-CAN-12197
- **Date:** 2021-02-24
- **CVE:** CVE-2020-16048
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Mozilla
- **Affected Products:** Firefox
- **Credit:** Abraruddin Khan and Omair
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-216/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Mozilla Firefox. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the implementation of the compressedTexImage3D API method in WebGL2. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Mozilla has issued an update to correct this vulnerability. More details can be found at: https://www.mozilla.org/en-US/security/advisories/mfsa2021-06/

## Disclosure Timeline

- 2020-11-11 - Vulnerability reported to vendor
- 2021-02-24 - Coordinated public release of advisory
