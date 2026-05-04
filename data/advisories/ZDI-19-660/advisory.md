# ZDI-19-660: (Pwn2Own) Xiaomi Browser miui.share APK Download Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-660
- **ZDI-CAN:** ZDI-CAN-7483
- **Date:** 2019-07-12
- **CVE:** CVE-2019-13322
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Xiaomi
- **Affected Products:** Browser
- **Credit:** MWR Labs - Georgi Geshev and Robert Miller
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-660/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Xiaomi Mi6 Browser. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the miui.share application. The issue results from the lack of proper validation of user-supplied data, which can result in an arbitrary application download. An attacker can leverage this vulnerability to execute code in the context of the user.

## Additional Details

This is resolved with Xiaomi Browser versionName:10.4.0, versionCode:20181211

## Disclosure Timeline

- 2019-07-11 - Vulnerability reported to vendor
- 2019-07-12 - Coordinated public release of advisory
- 2020-02-10 - Advisory Updated
