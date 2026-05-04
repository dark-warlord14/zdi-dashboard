# ZDI-22-1289: Apple macOS vImage ICC File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1289
- **ZDI-CAN:** ZDI-CAN-16520
- **Date:** 2022-09-19
- **CVE:** N/A
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Mickey Jin (@patch1t) of Trend Micro
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1289/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Apple macOS. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of ICC files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

According to Apple, ZDI-CAN-16520 was addressed in macOS Monterey 12.3 and iOS & iPadOS 15.4. Apple informed ZDI they would assign a CVE, but never followed through.

## Disclosure Timeline

- 2022-02-04 - Vulnerability reported to vendor
- 2022-09-19 - Coordinated public release of advisory
