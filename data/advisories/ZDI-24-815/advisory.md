# ZDI-24-815: Toshiba e-STUDIO2518A vsftpd Incorrect Permission Assignment Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-815
- **ZDI-CAN:** ZDI-CAN-23111
- **Date:** 2024-06-18
- **CVE:** CVE-2024-3498
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Toshiba
- **Affected Products:** e-STUDIO2518A
- **Credit:** Zhenhua Huang from trendmicro, Minmin Li
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-815/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on affected installations of Toshiba e-STUDIO2518A printers. Authentication is required to exploit this vulnerability. The specific flaw exists within the vsftpd daemon. The issue results from incorrect permissions set on folders. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of root.

## Additional Details

Toshiba has issued an update to correct this vulnerability. More details can be found at: https://www.toshibatec.com/information/20240531_01.html

## Disclosure Timeline

- 2024-02-14 - Vulnerability reported to vendor
- 2024-06-18 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
