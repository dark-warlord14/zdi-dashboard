# ZDI-25-192: Apple macOS MP4 File Parsing Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-192
- **ZDI-CAN:** ZDI-CAN-26494
- **Date:** 2025-04-01
- **CVE:** CVE-2025-24190
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Hossein Lotfi (@hosselot) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-192/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Apple macOS. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of MP4 files. The issue results from the lack of proper validation of user-supplied data, which can result in a memory corruption condition. An attacker can leverage this vulnerability to execute code in the context of the WebKit GPU process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/122373

## Disclosure Timeline

- 2025-02-07 - Vulnerability reported to vendor
- 2025-04-01 - Coordinated public release of advisory
- 2025-04-01 - Advisory Updated
