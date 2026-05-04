# ZDI-26-057: Apple Safari JavaScriptCore FTL New Array Materialization Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-057
- **ZDI-CAN:** ZDI-CAN-28285
- **Date:** 2026-02-03
- **CVE:** CVE-2025-46298
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** Hossein Lotfi (@hosselot) of Trend Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-057/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the new array materialization within FTL. By performing actions in JavaScript, an attacker can trigger a type confusion condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-ca/125890

## Disclosure Timeline

- 2025-10-15 - Vulnerability reported to vendor
- 2026-02-03 - Coordinated public release of advisory
- 2026-02-03 - Advisory Updated
