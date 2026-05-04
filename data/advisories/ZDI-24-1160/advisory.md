# ZDI-24-1160: Apple WebKit WebCodecs VideoFrame Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1160
- **ZDI-CAN:** ZDI-CAN-23730
- **Date:** 2024-08-22
- **CVE:** CVE-2024-40789
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** WebKit
- **Credit:** Seunghyun Lee (@0x10n) of KAIST Hacking Lab
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1160/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Apple WebKit. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the VideoFrame WebCodecs API. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/120913

## Disclosure Timeline

- 2024-05-01 - Vulnerability reported to vendor
- 2024-08-22 - Coordinated public release of advisory
- 2024-08-22 - Advisory Updated
