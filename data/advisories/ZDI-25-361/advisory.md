# ZDI-25-361: Trend Micro Password Manager Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-361
- **ZDI-CAN:** ZDI-CAN-25574
- **Date:** 2025-06-11
- **CVE:** CVE-2025-48443
- **CVSS:** 6.7
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Password Manager
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-361/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Trend Micro Password Manager. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. Additionally, the vulnerability is triggered only when an administrator performs an install of the product. The specific flaw exists within the product installer. By creating a junction, an attacker can abuse the installer to delete an arbitrary file. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://helpcenter.trendmicro.com/en-us/article/tmka-12917

## Disclosure Timeline

- 2025-01-14 - Vulnerability reported to vendor
- 2025-06-11 - Coordinated public release of advisory
- 2025-06-11 - Advisory Updated
