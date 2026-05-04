# ZDI-19-659: (Pwn2Own) Xiaomi Browser Captive Portal WebView Authorization Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-659
- **ZDI-CAN:** ZDI-CAN-7467
- **Date:** 2019-07-12
- **CVE:** CVE-2019-13321
- **CVSS:** 5.5
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:L
- **Affected Vendors:** Xiaomi
- **Affected Products:** Browser
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-659/
## Vulnerability Details

This vulnerability allows network adjacent attackers to execute arbitrary code on affected installations of Xiaomi Mi6. User interaction is required to exploit this vulnerability in that the target must connect to a malicious access point. The specific flaw exists within the handling of HTTP responses to the Captive Portal. A crafted HTML response can cause the Captive Portal to to open a browser to a specified location without user interaction. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

This is resolved with Xiaomi Browser versionName:10.4.0, versionCode:20181211

## Disclosure Timeline

- 2019-04-02 - Vulnerability reported to vendor
- 2019-07-12 - Coordinated public release of advisory
- 2020-02-10 - Advisory Updated
