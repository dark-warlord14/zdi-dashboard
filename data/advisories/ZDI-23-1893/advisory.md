# ZDI-23-1893: (0Day) Voltronic Power ViewPower Pro MySQL Use of Hard-coded Credentials Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1893
- **ZDI-CAN:** ZDI-CAN-22075
- **Date:** 2023-12-20
- **CVE:** CVE-2023-51588
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Voltronic Power
- **Affected Products:** ViewPower Pro
- **Credit:** 06fe5fd2bc53027c4a3b7e395af0b850e7b8a044
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1893/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Voltronic Power ViewPower Pro. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the configuration of a MySQL instance. The issue results from hardcoded database credentials. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

08/03/23 – ZDI made multiple attempts to contact the vendor across sales, support, and professional networking channels, which yielded no response from the vendor. We also contacted CISA, who was unsuccessful in receiving a response from the vendor. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2023-11-17 - Vulnerability reported to vendor
- 2023-12-20 - Coordinated public release of advisory
