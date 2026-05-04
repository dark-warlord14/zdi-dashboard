# ZDI-20-702: McAfee VirusScan Enterprise Junction Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-702
- **ZDI-CAN:** ZDI-CAN-10005
- **Date:** 2020-06-15
- **CVE:** CVE-2020-7280
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** McAfee
- **Affected Products:** VirusScan Enterprise
- **Credit:** Glenn Lloyd
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-702/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of McAfee VirusScan Enterprise. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the processing of log files. By creating a junction, an attacker can abuse the product to overwrite the contents of a chosen file. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of SYSTEM.

## Additional Details

McAfee has issued an update to correct this vulnerability. More details can be found at: https://kc.mcafee.com/corporate/index?page=content&id=SB10302

## Disclosure Timeline

- 2019-12-27 - Vulnerability reported to vendor
- 2020-06-15 - Coordinated public release of advisory
