# ZDI-23-914: NETGEAR ProSAFE Network Management System createUser Missing Authorization Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-914
- **ZDI-CAN:** ZDI-CAN-19726
- **Date:** 2023-07-13
- **CVE:** CVE-2023-38102
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NETGEAR
- **Affected Products:** ProSAFE Network Management System
- **Credit:** Steven Seeley of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-914/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on affected installations of NETGEAR ProSAFE Network Management System. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the createUser function. The issue results from the lack of authorization prior to allowing access to functionality. An attacker can leverage this vulnerability to escalate privileges to resources normally protected from the user.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000065707/Security-Advisory-for-Multiple-Vulnerabilities-on-the-ProSAFE-Network-Management-System-PSV-2023-0024-PSV-2023-0025

## Disclosure Timeline

- 2023-02-08 - Vulnerability reported to vendor
- 2023-07-13 - Coordinated public release of advisory
