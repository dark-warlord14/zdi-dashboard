# ZDI-24-1195: Malwarebytes Antimalware Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1195
- **ZDI-CAN:** ZDI-CAN-22321
- **Date:** 2024-09-05
- **CVE:** CVE-2024-6260
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Malwarebytes
- **Affected Products:** Anti-Malware
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1195/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Malwarebytes Antimalware. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Malwarebytes service. By creating a symbolic link, an attacker can abuse the service to delete a file. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Malwarebytes has issued an update to correct this vulnerability. More details can be found at: https://www.malwarebytes.com/secure/cves

## Disclosure Timeline

- 2024-06-04 - Vulnerability reported to vendor
- 2024-09-05 - Coordinated public release of advisory
- 2024-09-05 - Advisory Updated
