# ZDI-24-1720: (0Day) Arista NG Firewall uvm_login Incorrect Authorization Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1720
- **ZDI-CAN:** ZDI-CAN-24324
- **Date:** 2024-12-19
- **CVE:** CVE-2024-12831
- **CVSS:** 6.6
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:L/A:L
- **Affected Vendors:** Arista
- **Affected Products:** NG Firewall
- **Credit:** Mehmet INCE (@mdisec) from PRODAFT.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1720/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Arista NG Firewall. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the uvm_login module. The issue results from incorrect authorization. An attacker can leverage this to escalate privileges to resources normally protected from the user.

## Additional Details

07/03/24 – ZDI reported the vulnerability to the vendor 08/07/24 – the vendor acknowledged the receipt of the report 11/18/24 - ZDI asked for updates 11/21/24 - ZDI asked for updates 12/10/24 - ZDI notified the vendor of the intention to publish the cases as a 0-day advisory Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application

## Disclosure Timeline

- 2024-07-03 - Vulnerability reported to vendor
- 2024-12-19 - Coordinated public release of advisory
- 2024-12-19 - Advisory Updated
