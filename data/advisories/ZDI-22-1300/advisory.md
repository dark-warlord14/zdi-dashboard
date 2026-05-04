# ZDI-22-1300: Windscribe Uncontrolled Search Path Element Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1300
- **ZDI-CAN:** ZDI-CAN-16859
- **Date:** 2022-09-26
- **CVE:** CVE-2022-41141
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Windscribe
- **Affected Products:** Windscribe
- **Credit:** Xavier DANEST
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1300/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Windscribe. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the configuration of OpenSSL. The product loads an OpenSSL configuration file from an unsecured location. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Windscribe has issued an update to correct this vulnerability. More details can be found at: https://windscribe.com/changelog/windows

## Disclosure Timeline

- 2022-03-17 - Vulnerability reported to vendor
- 2022-09-26 - Coordinated public release of advisory
