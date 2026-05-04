# ZDI-24-803: Parallels Desktop Updater Protection Mechanism Failure Software Downgrade Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-803
- **ZDI-CAN:** ZDI-CAN-19481
- **Date:** 2024-06-18
- **CVE:** CVE-2024-6153
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Parallels
- **Affected Products:** Desktop
- **Credit:** aegis
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-803/
## Vulnerability Details

This vulnerability allows local attackers to downgrade Parallels software on affected installations of Parallels Desktop. An attacker must first obtain the ability to execute low-privileged code on the target host system in order to exploit this vulnerability. The specific flaw exists within the Updater service. The issue results from the lack of proper validation of version information before performing an update. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges and execute arbitrary code in the context of root.

## Additional Details

https://kb.parallels.com/129060 18.3.0 (53606)

## Disclosure Timeline

- 2022-11-30 - Vulnerability reported to vendor
- 2024-06-18 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
