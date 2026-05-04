# ZDI-25-047: WinZip 7Z File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-047
- **ZDI-CAN:** ZDI-CAN-24986
- **Date:** 2025-02-11
- **CVE:** CVE-2025-1240
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** WinZip Computing
- **Affected Products:** WinZip
- **Credit:** Jan Kopecky
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-047/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of WinZip. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of 7Z files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

This vulnerability has been patched for the subscription and perpetual license versions listed below Subscription: 76.8 and later versions Perpetual license versions: * 29.0 and later versions * 28.0.16371 and later versions * 27.0.16370 and later versions https://kb.winzip.com/help/help_whatsnew.htm

## Disclosure Timeline

- 2024-09-04 - Vulnerability reported to vendor
- 2025-02-11 - Coordinated public release of advisory
- 2025-05-02 - Advisory Updated
