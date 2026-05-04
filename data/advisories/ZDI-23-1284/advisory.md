# ZDI-23-1284: NETGEAR ProSAFE Network Management System ZipUtils Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1284
- **ZDI-CAN:** ZDI-CAN-19716
- **Date:** 2023-08-30
- **CVE:** CVE-2023-41182
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NETGEAR
- **Affected Products:** ProSAFE Network Management System
- **Credit:** Steven Seeley of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1284/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of NETGEAR ProSAFE Network Management System. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the ZipUtils class. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000065705/Security-Advisory-for-Post-authentication-Command-Injection-on-the-Prosafe-Network-Management-System-PSV-2023-0037

## Disclosure Timeline

- 2023-02-17 - Vulnerability reported to vendor
- 2023-08-30 - Coordinated public release of advisory
