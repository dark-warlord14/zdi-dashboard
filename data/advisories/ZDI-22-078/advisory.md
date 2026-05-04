# ZDI-22-078: Fortinet FortiClient Network Access Control Uncontrolled Search Path Element Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-078
- **ZDI-CAN:** ZDI-CAN-14137
- **Date:** 2022-01-17
- **CVE:** CVE-2021-26089
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Fortinet
- **Affected Products:** FortiClient
- **Credit:** brsn
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-078/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Fortinet FortiClient Network Access Control. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Network Access Control service. The service loads an OpenSSL configuration file from an unsecured location. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Fortinet has issued an update to correct this vulnerability. More details can be found at: https://www.fortiguard.com/psirt/FG-IR-21-022

## Disclosure Timeline

- 2021-07-30 - Vulnerability reported to vendor
- 2022-01-17 - Coordinated public release of advisory
