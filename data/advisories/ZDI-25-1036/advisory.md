# ZDI-25-1036: Tencent TFace restore_checkpoint Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1036
- **ZDI-CAN:** ZDI-CAN-27185
- **Date:** 2025-12-01
- **CVE:** CVE-2025-13709
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Tencent
- **Affected Products:** TFace
- **Credit:** Peter Girnus (@gothburz) of Trend Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1036/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Tencent TFace. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the restore_checkpoint function. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Tencent has issued an update to correct this vulnerability. More details can be found at: https://github.com/Tencent/TFace/commit/7b2eed297d43dcdd1e3d45bfdfc950478e3af5d9

## Disclosure Timeline

- 2025-05-22 - Vulnerability reported to vendor
- 2025-12-01 - Coordinated public release of advisory
- 2025-12-01 - Advisory Updated
