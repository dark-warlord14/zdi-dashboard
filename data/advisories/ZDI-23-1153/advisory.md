# ZDI-23-1153: 3CX Uncontrolled Search Path Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1153
- **ZDI-CAN:** ZDI-CAN-20026
- **Date:** 2023-08-21
- **CVE:** CVE-2023-27362
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** 3CX
- **Affected Products:** 3CX
- **Credit:** Xavier DANEST
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1153/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of 3CX. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the configuration of OpenSSL. The product loads an OpenSSL configuration file from an unsecured location. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

3CX has issued an update to correct this vulnerability. More details can be found at: https://www.3cx.com/blog/releases/v18-u8/

## Disclosure Timeline

- 2023-04-17 - Vulnerability reported to vendor
- 2023-08-21 - Coordinated public release of advisory
