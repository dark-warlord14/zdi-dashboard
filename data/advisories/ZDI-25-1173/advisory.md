# ZDI-25-1173: Foxit PDF Reader Update Service Incorrect Permission Assignment Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1173
- **ZDI-CAN:** ZDI-CAN-28053
- **Date:** 2025-12-19
- **CVE:** CVE-2025-13941
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Foxit
- **Affected Products:** PDF Reader
- **Credit:** kozmer
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1173/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Foxit PDF Reader. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of the plugins installed by the Foxit Reader Update Service. The issue results from incorrect permissions set on a resource used by the service. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of SYSTEM.

## Additional Details

https://www.foxit.com/support/security-bulletins.html

## Disclosure Timeline

- 2025-10-07 - Vulnerability reported to vendor
- 2025-12-19 - Coordinated public release of advisory
- 2025-12-19 - Advisory Updated
