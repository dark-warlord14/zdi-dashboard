# ZDI-24-814: Toshiba e-STUDIO2518A unzip Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-814
- **ZDI-CAN:** ZDI-CAN-23109
- **Date:** 2024-06-18
- **CVE:** CVE-2024-3497
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Toshiba
- **Affected Products:** e-STUDIO2518A
- **Credit:** Zhenhua Huang from trendmicro, Minmin Li
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-814/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Toshiba e-STUDIO2518A printers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the unzip method. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Toshiba has issued an update to correct this vulnerability. More details can be found at: https://www.toshibatec.com/information/20240531_01.html

## Disclosure Timeline

- 2024-02-14 - Vulnerability reported to vendor
- 2024-06-18 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
