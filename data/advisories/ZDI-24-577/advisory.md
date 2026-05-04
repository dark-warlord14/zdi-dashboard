# ZDI-24-577: Trend Micro Apex One Improper Access Control Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-577
- **ZDI-CAN:** ZDI-CAN-21599
- **Date:** 2024-06-06
- **CVE:** CVE-2024-37289
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Apex One
- **Credit:** NT AUTHORITY\ANONYMOUS LOGON
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-577/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Trend Micro Apex One. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Apex One Security Agent. The specific flaw exists within the logic that controls access to the Suspect folder. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/dcx/s/solution/000298063

## Disclosure Timeline

- 2023-08-22 - Vulnerability reported to vendor
- 2024-06-06 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
