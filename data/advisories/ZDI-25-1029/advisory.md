# ZDI-25-1029: Tencent HunyuanDiT model_resume Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1029
- **ZDI-CAN:** ZDI-CAN-27183
- **Date:** 2025-12-01
- **CVE:** CVE-2025-13707
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Tencent
- **Affected Products:** HunyuanDiT
- **Credit:** Peter Girnus (@gothburz) of Trend Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1029/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Tencent HunyuanDiT. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the model_resume function. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Tencent has issued an update to correct this vulnerability. More details can be found at: https://github.com/Tencent-Hunyuan/HunyuanDiT/commit/d2cb9cde5c9dc6a6c01735dcb92fe7699ddf6bc5

## Disclosure Timeline

- 2025-05-22 - Vulnerability reported to vendor
- 2025-12-01 - Coordinated public release of advisory
- 2025-12-01 - Advisory Updated
