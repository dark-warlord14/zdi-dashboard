# ZDI-25-1030: Tencent HunyuanVideo load_vae Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1030
- **ZDI-CAN:** ZDI-CAN-27186
- **Date:** 2025-12-01
- **CVE:** CVE-2025-13710
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Tencent
- **Affected Products:** HunyuanVideo
- **Credit:** Peter Girnus (@gothburz) of Trend Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1030/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Tencent HunyuanVideo. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the load_vae function.The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Tencent has issued an update to correct this vulnerability. More details can be found at: https://github.com/Tencent-Hunyuan/HunyuanVideo/commit/b47e10b95483aa8458b64d23350844c29e91c408

## Disclosure Timeline

- 2025-05-22 - Vulnerability reported to vendor
- 2025-12-01 - Coordinated public release of advisory
- 2025-12-01 - Advisory Updated
