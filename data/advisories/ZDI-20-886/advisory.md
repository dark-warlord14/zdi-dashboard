# ZDI-20-886: Oracle VirtualBox Guest Additions Unnecessary Privileges Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-886
- **ZDI-CAN:** ZDI-CAN-10762
- **Date:** 2020-07-20
- **CVE:** CVE-2020-14628
- **CVSS:** 8.2
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** Conor McErlane
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-886/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Oracle VirtualBox. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Guest Additions toolset. The issue results from the use of unnecessary privileges when performing service operations. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of SYSTEM.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpujul2020.html

## Disclosure Timeline

- 2020-04-14 - Vulnerability reported to vendor
- 2020-07-20 - Coordinated public release of advisory
