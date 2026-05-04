# ZDI-25-835: NoMachine Uncontrolled Search Path Element Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-835
- **ZDI-CAN:** ZDI-CAN-26766
- **Date:** 2025-08-13
- **CVE:** CVE-2025-8614
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NoMachine
- **Affected Products:** NoMachine
- **Credit:** Xavier DANEST
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-835/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of NoMachine. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the configuration of OpenSSL. The product loads an OpenSSL configuration file from an unsecured location. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the service account.

## Additional Details

NoMachine has issued an update to correct this vulnerability. More details can be found at: https://kb.nomachine.com/TR04W11314

## Disclosure Timeline

- 2025-04-25 - Vulnerability reported to vendor
- 2025-08-13 - Coordinated public release of advisory
- 2025-09-02 - Advisory Updated
