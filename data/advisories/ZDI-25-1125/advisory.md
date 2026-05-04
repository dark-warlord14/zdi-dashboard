# ZDI-25-1125: Trend Micro Cleaner One Pro Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1125
- **ZDI-CAN:** ZDI-CAN-27644
- **Date:** 2025-12-17
- **CVE:** CVE-2025-53503
- **CVSS:** 7.3
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Cleaner One Pro
- **Credit:** Zeze and Sharkkcode with TeamT5
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1125/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Trend Micro Cleaner One Pro. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Junk Files Cleanup functionality. By creating a junction, an attacker can abuse the service to delete arbitrary files. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://helpcenter.trendmicro.com/en-us/article/tmka-12951

## Disclosure Timeline

- 2025-08-14 - Vulnerability reported to vendor
- 2025-12-17 - Coordinated public release of advisory
- 2025-12-17 - Advisory Updated
