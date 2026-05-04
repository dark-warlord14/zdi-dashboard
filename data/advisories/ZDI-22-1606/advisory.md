# ZDI-22-1606: (Pwn2Own) Microsoft Teams pluginHost Sandbox Escape Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1606
- **ZDI-CAN:** ZDI-CAN-17467
- **Date:** 2022-11-21
- **CVE:** N/A
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Teams
- **Credit:** Masato Kinugawa
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1606/
## Vulnerability Details

This vulnerability allows remote attackers to escape the sandbox on affected installations of Microsoft Teams. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the pluginHost component. The component exposes a WebView that allows an attacker to invoke arbitrary RPC calls. An attacker can leverage this vulnerability to escape the sandbox and execute arbitrary code in the context of the current process.

## Additional Details

Fixed on August 31, 2022 https://msrc.microsoft.com/update-guide/acknowledgement/online

## Disclosure Timeline

- 2022-05-25 - Vulnerability reported to vendor
- 2022-11-21 - Coordinated public release of advisory
