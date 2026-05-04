# ZDI-25-728: Apple macOS MediaToolbox Framework Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-728
- **ZDI-CAN:** ZDI-CAN-26782
- **Date:** 2025-07-30
- **CVE:** CVE-2025-31239
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Hossein Lotfi (@hosselot) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-728/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Apple macOS. Interaction with the MediaToolbox framework is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the implementation of audio decoding. The issue results from the lack of proper validation of user-supplied data, which can result in a memory corruption condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/122716

## Disclosure Timeline

- 2025-03-25 - Vulnerability reported to vendor
- 2025-07-30 - Coordinated public release of advisory
- 2025-07-30 - Advisory Updated
