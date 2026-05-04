# ZDI-24-418: (Pwn2Own) Xiaomi Pro 13 mimarket manual-upgrade Cross-Site Scripting Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-418
- **ZDI-CAN:** ZDI-CAN-22379
- **Date:** 2024-05-01
- **CVE:** CVE-2024-4405
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Xiaomi
- **Affected Products:** Pro 13
- **Credit:** @hoangnx99, @vudq16, @biennd279, @_q5ca from @vcslab
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-418/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Xiaomi Pro 13 smartphones. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the manual-upgrade.html file. When parsing the manualUpgradeInfo parameter, the process does not properly sanitize user-supplied data, which can lead to the injection of an arbitrary script. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

According to Xiaomi, ZDI-CAN-22379 was addressed in GetApps 32.0.0.1. Xiaomi informed ZDI they would assign a CVE, but never followed through.

## Disclosure Timeline

- 2023-11-09 - Vulnerability reported to vendor
- 2024-05-01 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
