# ZDI-20-1389: Apple macOS CoreGraphics JBIG2Stream Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1389
- **ZDI-CAN:** ZDI-CAN-11210
- **Date:** 2020-12-03
- **CVE:** CVE-2020-9883
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Mickey Jin of Trend Micro Mobile Security Research Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1389/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Apple macOS. Interaction with the CoreGraphics library is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the JBIG2Stream::readGenericBitmap method. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated data structure. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT211294

## Disclosure Timeline

- 2020-06-05 - Vulnerability reported to vendor
- 2020-12-03 - Coordinated public release of advisory
