# ZDI-23-646: Apple WebKit WebGL2 drawRangeElements Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-646
- **ZDI-CAN:** ZDI-CAN-17329
- **Date:** 2023-05-17
- **CVE:** CVE-2022-32912
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** WebKit
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-646/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Apple WebKit. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the implementation of the drawRangeElements method in WebGL2. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/HT213442

## Disclosure Timeline

- 2022-06-24 - Vulnerability reported to vendor
- 2023-05-17 - Coordinated public release of advisory
- 2024-07-08 - Advisory Updated
