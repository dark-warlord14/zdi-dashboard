# ZDI-24-1298: Foxit PDF Reader Update Service Incorrect Permission Assignment Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1298
- **ZDI-CAN:** ZDI-CAN-23933
- **Date:** 2024-09-26
- **CVE:** CVE-2024-9244
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Foxit
- **Affected Products:** PDF Reader
- **Credit:** EthicalChaos
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1298/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Foxit PDF Reader. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of the configuration files used by the Foxit Reader Update Service. The issue results from incorrect permissions set on a resource used by the service. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of SYSTEM.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxit.com/support/security-bulletins.html

## Disclosure Timeline

- 2024-05-15 - Vulnerability reported to vendor
- 2024-09-26 - Coordinated public release of advisory
- 2024-09-26 - Advisory Updated
