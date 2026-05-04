# ZDI-23-915: NETGEAR ProSAFE Network Management System SettingConfigController Exposed Dangerous Function Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-915
- **ZDI-CAN:** ZDI-CAN-19725
- **Date:** 2023-07-13
- **CVE:** CVE-2023-38101
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NETGEAR
- **Affected Products:** ProSAFE Network Management System
- **Credit:** Steven Seeley of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-915/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of NETGEAR ProSAFE Network Management System. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the SettingConfigController class. The issue results from an exposed dangerous function. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000065707/Security-Advisory-for-Multiple-Vulnerabilities-on-the-ProSAFE-Network-Management-System-PSV-2023-0024-PSV-2023-0025

## Disclosure Timeline

- 2023-02-08 - Vulnerability reported to vendor
- 2023-07-13 - Coordinated public release of advisory
