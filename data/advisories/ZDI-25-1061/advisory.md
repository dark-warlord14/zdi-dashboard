# ZDI-25-1061: Windscribe Uncontrolled Search Path Element Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1061
- **ZDI-CAN:** ZDI-CAN-27873
- **Date:** 2025-12-10
- **CVE:** CVE-2025-14400
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Windscribe
- **Affected Products:** Windscribe
- **Credit:** Xavier DANEST
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1061/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Windscribe. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the configuration of OpenSSL. The product loads an OpenSSL configuration file from an unsecured location. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Windscribe has issued an update to correct this vulnerability. More details can be found at: https://github.com/Windscribe/Desktop-App/releases/tag/v2.17.10

## Disclosure Timeline

- 2025-08-14 - Vulnerability reported to vendor
- 2025-12-10 - Coordinated public release of advisory
- 2025-12-10 - Advisory Updated
