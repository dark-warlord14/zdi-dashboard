# ZDI-20-287: (Pwn2Own) Xiaomi Mi9 Browser Untrusted Site Redirection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-287
- **ZDI-CAN:** ZDI-CAN-9656
- **Date:** 2020-03-12
- **CVE:** CVE-2020-9531
- **CVSS:** 5.5
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:L
- **Affected Vendors:** Xiaomi
- **Affected Products:** Browser
- **Credit:** @FSecureLabs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-287/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Xiaomi Mi9 Browser. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within Xiaomi GetApps webview. By manipulating HTML, an attacker can force a page redirection. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fixed in v 2001122

## Disclosure Timeline

- 2019-11-19 - Vulnerability reported to vendor
- 2020-03-12 - Coordinated public release of advisory
