# ZDI-26-281: Microsoft vcpkg OpenSSL Uncontrolled Search Path Element Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-281
- **ZDI-CAN:** ZDI-CAN-29616
- **Date:** 2026-04-15
- **CVE:** CVE-2026-34054
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** vcpkg
- **Credit:** Xavier DANEST
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-281/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on applications built using the Microsoft vcpkg port of OpenSSL. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the configuration of OpenSSL. The product loads configuration from an unsecured location. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of a target process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://github.com/microsoft/vcpkg/security/advisories/GHSA-p322-v6vw-vrq9

## Disclosure Timeline

- 2026-03-10 - Vulnerability reported to vendor
- 2026-04-15 - Coordinated public release of advisory
- 2026-04-15 - Advisory Updated
