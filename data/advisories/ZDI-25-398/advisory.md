# ZDI-25-398: Trend Micro Internet Security Platinum Host Service Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-398
- **ZDI-CAN:** ZDI-CAN-25876
- **Date:** 2025-06-17
- **CVE:** CVE-2025-49384
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Internet Security
- **Credit:** Vladislav Berghici of Trend Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-398/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Trend Micro Internet Security. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Platinum Host Service. By creating a symbolic link, an attacker can abuse the service to delete a file. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://helpcenter.trendmicro.com/en-us/article/TMKA-11112

## Disclosure Timeline

- 2024-12-06 - Vulnerability reported to vendor
- 2025-06-17 - Coordinated public release of advisory
- 2025-06-17 - Advisory Updated
