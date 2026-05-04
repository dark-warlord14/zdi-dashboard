# ZDI-19-366: (Pwn2Own) Xiaomi Mi6 Browser WebAssembly.Instance Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-366
- **ZDI-CAN:** ZDI-CAN-7466
- **Date:** 2019-04-15
- **CVE:** CVE-2019-6743
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Xiaomi
- **Affected Products:** Browser
- **Credit:** fluoroacetate
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-366/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Xiaomi Mi6 Browser. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the WebAssembly.Instance method. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of a heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

This is resolved with Xiaomi Browser versionName:10.4.0, versionCode:20181211.

## Disclosure Timeline

- 2018-11-15 - Vulnerability reported to vendor
- 2019-04-15 - Coordinated public release of advisory
- 2019-06-14 - Advisory Updated
