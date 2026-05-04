# ZDI-22-357: Apple macOS CoreGraphics PDF File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-357
- **ZDI-CAN:** ZDI-CAN-14385
- **Date:** 2022-02-16
- **CVE:** CVE-2021-30919
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Jzhu
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-357/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Apple macOS. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of PDF files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/HT212872

## Disclosure Timeline

- 2021-07-13 - Vulnerability reported to vendor
- 2022-02-16 - Coordinated public release of advisory
