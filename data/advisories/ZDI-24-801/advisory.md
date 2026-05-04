# ZDI-24-801: Tenable Nessus Network Monitor Uncontrolled Search Path Element Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-801
- **ZDI-CAN:** ZDI-CAN-21959
- **Date:** 2024-06-18
- **CVE:** CVE-2023-5622
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Tenable
- **Affected Products:** Nessus Network Monitor
- **Credit:** Xavier DANEST - Decathlon
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-801/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Tenable Nessus Network Monitor. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the configuration of OpenSSL. The process loads an OpenSSL configuration file from an unsecured location. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Tenable has issued an update to correct this vulnerability. More details can be found at: https://www.tenable.com/security/tns-2023-34

## Disclosure Timeline

- 2023-10-06 - Vulnerability reported to vendor
- 2024-06-18 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
