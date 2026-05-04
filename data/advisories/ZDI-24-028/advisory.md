# ZDI-24-028: Trend Micro Apex One Security Agent Updater Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-028
- **ZDI-CAN:** ZDI-CAN-21896
- **Date:** 2024-01-10
- **CVE:** CVE-2023-52094
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Apex One
- **Credit:** NT AUTHORITY\ANONYMOUS LOGON
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-028/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Trend Micro Apex One Security Agent. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the product update mechanism. By creating a junction, an attacker can abuse the updater to delete a folder. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/000296151

## Disclosure Timeline

- 2023-08-17 - Vulnerability reported to vendor
- 2024-01-10 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
