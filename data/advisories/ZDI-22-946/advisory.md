# ZDI-22-946: Parallels Access Agent Uncontrolled Search Path Element Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-946
- **ZDI-CAN:** ZDI-CAN-15787
- **Date:** 2022-07-01
- **CVE:** CVE-2022-34902
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Parallels
- **Affected Products:** Access
- **Credit:** Xavier Danest - Decathlon
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-946/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Parallels Access Agent. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Desktop Control Agent service. The service loads Qt plugins from an unsecured location. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Parallels has issued an update to correct this vulnerability. More details can be found at: https://kb.parallels.com/en/129010

## Disclosure Timeline

- 2021-12-22 - Vulnerability reported to vendor
- 2022-07-01 - Coordinated public release of advisory
