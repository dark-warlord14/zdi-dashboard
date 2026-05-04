# ZDI-25-586: Trend Micro Password Manager Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-586
- **ZDI-CAN:** ZDI-CAN-25729
- **Date:** 2025-07-08
- **CVE:** CVE-2025-52837
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Password Manager
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-586/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Trend Micro Password Manager. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Trend Micro Password Manager Service. By creating a junction, an attacker can abuse the installer to delete an arbitrary file. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://helpcenter.trendmicro.com/en-us/article/TMKA-12946

## Disclosure Timeline

- 2025-02-13 - Vulnerability reported to vendor
- 2025-07-08 - Coordinated public release of advisory
- 2025-07-08 - Advisory Updated
