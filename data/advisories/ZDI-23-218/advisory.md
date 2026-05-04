# ZDI-23-218: Parallels Desktop Updater Improper Initialization Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-218
- **ZDI-CAN:** ZDI-CAN-18229
- **Date:** 2023-03-07
- **CVE:** CVE-2023-27324
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Parallels
- **Affected Products:** Desktop
- **Credit:** kn32
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-218/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Parallels Desktop. An attacker must first obtain the ability to execute low-privileged code on the target host system in order to exploit this vulnerability. The specific flaw exists within the Updater service. The issue results from the lack of proper initialization of environment variables. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of root.

## Additional Details

Parallels has issued an update to correct this vulnerability. More details can be found at: https://kb.parallels.com/125013

## Disclosure Timeline

- 2022-08-31 - Vulnerability reported to vendor
- 2023-03-07 - Coordinated public release of advisory
