# ZDI-23-1582: Tenable Nessus Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1582
- **ZDI-CAN:** ZDI-CAN-21965
- **Date:** 2023-11-06
- **CVE:** CVE-2023-5847
- **CVSS:** 6.7
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Tenable
- **Affected Products:** Nessus
- **Credit:** Xavier DANEST - Decathlon
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1582/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Tenable Nessus. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the configuration of OpenSSL. The process loads an OpenSSL configuration file from an unsecured location. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Fixed in Nessus 10.6.2 / 10.5.6 and Nessus Agent 10.4.3 https://www.tenable.com/security/tns-2023-36 https://www.tenable.com/security/tns-2023-37 https://www.tenable.com/security/tns-2023-38

## Disclosure Timeline

- 2023-10-06 - Vulnerability reported to vendor
- 2023-11-06 - Coordinated public release of advisory
