# ZDI-24-1412: Oracle VirtualBox Shared Folders Incorrect Authorization Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1412
- **ZDI-CAN:** ZDI-CAN-24045
- **Date:** 2024-10-17
- **CVE:** CVE-2024-21248
- **CVSS:** 5.3
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:C/C:L/I:L/A:L
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1412/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Oracle VirtualBox. An attacker must first obtain the ability to execute low-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the implementation of Shared Folders. The issue results from incorrect authorization. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the current user on the host system.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpuoct2024verbose.html

## Disclosure Timeline

- 2024-07-12 - Vulnerability reported to vendor
- 2024-10-17 - Coordinated public release of advisory
- 2024-10-17 - Advisory Updated
