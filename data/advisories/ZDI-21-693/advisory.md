# ZDI-21-693: Fortinet FortiClient Incorrect Permission Assignment Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-693
- **ZDI-CAN:** ZDI-CAN-12128
- **Date:** 2021-06-17
- **CVE:** CVE-2021-26089
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Fortinet
- **Affected Products:** FortiClient
- **Credit:** Csaba Fitzl (@theevilbit) of Offensive Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-693/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Fortinet FortiClient on Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the FortiClient installer. The issue lies in the lack of proper permissions set on log files created by the installer. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of root.

## Additional Details

Fixed in version 7.0.0

## Disclosure Timeline

- 2021-02-03 - Vulnerability reported to vendor
- 2021-06-17 - Coordinated public release of advisory
