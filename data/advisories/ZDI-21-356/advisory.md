# ZDI-21-356: NETGEAR ProSAFE Network Management System SettingConfigController fileName Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-356
- **ZDI-CAN:** ZDI-CAN-12121
- **Date:** 2021-03-26
- **CVE:** CVE-2021-27273
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NETGEAR
- **Affected Products:** ProSAFE Network Management System
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-356/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of NETGEAR ProSAFE Network Management System. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the SettingConfigController class. When parsing the fileName parameter, the process does not properly validate a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000062686/Security-Advisory-for-Post-Authentication-Command-Injection-on-NMS300-PSV-2020-0559

## Disclosure Timeline

- 2020-10-30 - Vulnerability reported to vendor
- 2021-03-26 - Coordinated public release of advisory
