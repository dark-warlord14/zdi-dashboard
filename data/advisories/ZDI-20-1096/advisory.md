# ZDI-20-1096: Trend Micro Apex One Hard Link Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1096
- **ZDI-CAN:** ZDI-CAN-10790
- **Date:** 2020-08-31
- **CVE:** CVE-2020-24559
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Apex One
- **Credit:** @Kharosx0
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1096/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Trend Micro Apex One. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the ApexOne Security Agent. By creating a hard link, an attacker can abuse the service to overwrite the contents of a chosen file. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of root.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/000263632

## Disclosure Timeline

- 2020-04-16 - Vulnerability reported to vendor
- 2020-08-31 - Coordinated public release of advisory
