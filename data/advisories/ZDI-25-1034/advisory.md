# ZDI-25-1034: Tencent PatrickStar merge_checkpoint Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1034
- **ZDI-CAN:** ZDI-CAN-27182
- **Date:** 2025-12-01
- **CVE:** CVE-2025-13706
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Tencent
- **Affected Products:** PatrickStar
- **Credit:** Peter Girnus (@gothburz) of Trend Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1034/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Tencent PatrickStar. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the merge_checkpoint endpoint. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Tencent has issued an update to correct this vulnerability. More details can be found at: https://github.com/Tencent/PatrickStar/commit/2384535503ea98cfe35ad04e20c0cfc7bf58d5d7

## Disclosure Timeline

- 2025-05-29 - Vulnerability reported to vendor
- 2025-12-01 - Coordinated public release of advisory
- 2025-12-01 - Advisory Updated
