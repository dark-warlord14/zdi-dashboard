# ZDI-26-138: Trend Micro Apex One Virus Scan Engine Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-138
- **ZDI-CAN:** ZDI-CAN-24972
- **Date:** 2026-03-03
- **CVE:** CVE-2025-71212
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Apex One
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-138/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Trend Micro Apex One Security Agent. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Virus Scan Engine. By creating a symbolic link, an attacker can abuse the VSApiNt.sys driver to delete arbitrary files. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/en-US/solution/KA-0022458

## Disclosure Timeline

- 2024-08-14 - Vulnerability reported to vendor
- 2026-03-03 - Coordinated public release of advisory
- 2026-03-03 - Advisory Updated
