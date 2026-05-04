# ZDI-23-1583: Google Chromium Vulkan SwiftShader Double Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1583
- **ZDI-CAN:** ZDI-CAN-22148
- **Date:** 2023-11-06
- **CVE:** N/A
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Google
- **Affected Products:** Chromium
- **Credit:** Dohyun Lee (@l33d0hyun)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1583/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Google Chromium-based browsers. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within Vulkan SwiftShader. The issue results from the lack of validating the existence of an object prior to performing further free operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fixed in Chrome 117 https://swiftshader-review.googlesource.com/c/SwiftShader/+/71928

## Disclosure Timeline

- 2023-09-14 - Vulnerability reported to vendor
- 2023-11-06 - Coordinated public release of advisory
- 2023-11-07 - Advisory Updated
