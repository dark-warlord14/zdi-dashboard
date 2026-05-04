# ZDI-19-368: (Pwn2Own) Xiaomi Mi6 V8 CollectValuesOrEntriesImpl Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-368
- **ZDI-CAN:** ZDI-CAN-7478
- **Date:** 2019-04-17
- **CVE:** CVE-2018-6064
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Xiaomi
- **Affected Products:** Browser
- **Credit:** Michael Contreras
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-368/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Xiaomi Mi6. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the CollectValuesOrEntriesImpl function. By performing actions in JavaScript, an attacker can trigger a type confusion condition. An attacker can leverage this vulnerability to execute code in the context of current process.

## Additional Details

This is resolved with Xiaomi Browser versionName:10.4.0, versionCode:20181211.

## Disclosure Timeline

- 2018-11-15 - Vulnerability reported to vendor
- 2019-04-17 - Coordinated public release of advisory
- 2019-06-14 - Advisory Updated
