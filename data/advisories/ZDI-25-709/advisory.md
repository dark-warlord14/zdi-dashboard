# ZDI-25-709: Apple Safari JavaScriptCore WasmToJSException Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-709
- **ZDI-CAN:** ZDI-CAN-27217
- **Date:** 2025-07-29
- **CVE:** CVE-2025-43214
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** shandikri
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-709/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the WasmToJSException operation. By performing actions in JavaScript, an attacker can trigger a type confusion condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/124149

## Disclosure Timeline

- 2025-06-10 - Vulnerability reported to vendor
- 2025-07-29 - Coordinated public release of advisory
- 2025-08-26 - Advisory Updated
