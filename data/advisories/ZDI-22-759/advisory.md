# ZDI-22-759: Trend Micro Password Manager Link Following Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-759
- **ZDI-CAN:** ZDI-CAN-16159
- **Date:** 2022-05-11
- **CVE:** CVE-2022-30523
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Password Manager
- **Credit:** @Kharosx0
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-759/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Trend Micro Password Manager. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Trend Micro Password Manager Service. By creating a symbolic link, an attacker can abuse the service to delete a file. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://helpcenter.trendmicro.com/en-us/article/tmka-09071

## Disclosure Timeline

- 2022-01-07 - Vulnerability reported to vendor
- 2022-05-11 - Coordinated public release of advisory
