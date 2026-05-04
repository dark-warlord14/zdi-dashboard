# ZDI-25-1183: Tencent FaceDetection-DSFD resnet Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1183
- **ZDI-CAN:** ZDI-CAN-27197
- **Date:** 2025-12-23
- **CVE:** CVE-2025-13715
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Tencent
- **Affected Products:** FaceDetection-DSFD
- **Credit:** Peter Girnus (@gothburz) of Trend Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1183/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Tencent FaceDetection-DSFD. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the resnet endpoint. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Tencent has issued an update to correct this vulnerability. More details can be found at: https://github.com/Tencent/FaceDetection-DSFD/commit/a941d089d8ae2df5292a904e79d88649cb58a440

## Disclosure Timeline

- 2025-05-22 - Vulnerability reported to vendor
- 2025-12-23 - Coordinated public release of advisory
- 2025-12-23 - Advisory Updated
