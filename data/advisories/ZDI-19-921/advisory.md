# ZDI-19-921: (Pwn2Own) Google Chromium RegExpReplace Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-921
- **ZDI-CAN:** ZDI-CAN-8378
- **Date:** 2019-10-29
- **CVE:** CVE-2019-13698
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Google
- **Affected Products:** Chromium
- **Credit:** fluoroacetate (@fluoroacetate)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-921/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Google Chromium. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the implementation of the JavaScript RegExp.replace method. By performing actions in JavaScript, an attacker can trigger a type confusion condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Google has issued an update to correct this vulnerability. More details can be found at: https://chromereleases.googleblog.com/2019/04/stable-channel-update-for-desktop.html

## Disclosure Timeline

- 2019-10-29 - Vulnerability reported to vendor
- 2019-10-29 - Coordinated public release of advisory
