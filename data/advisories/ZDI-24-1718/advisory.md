# ZDI-24-1718: (0Day) Arista NG Firewall custom_handler Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1718
- **ZDI-CAN:** ZDI-CAN-24019
- **Date:** 2024-12-19
- **CVE:** CVE-2024-12830
- **CVSS:** 8.1
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Arista
- **Affected Products:** NG Firewall
- **Credit:** Mehmet INCE (@mdisec) from PRODAFT
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1718/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Arista NG Firewall. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of the custom_handler method. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of the www-data user.

## Additional Details

07/03/24 – ZDI reported the vulnerability to the vendor 08/07/24 – the vendor acknowledged the receipt of the report 11/18/24 - ZDI asked for updates 11/21/24 - ZDI asked for updates 12/10/24 - ZDI notified the vendor of the intention to publish the cases as a 0-day advisory Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application

## Disclosure Timeline

- 2024-07-03 - Vulnerability reported to vendor
- 2024-12-19 - Coordinated public release of advisory
- 2024-12-19 - Advisory Updated
