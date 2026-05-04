# ZDI-24-1717: (0Day) Arista NG Firewall ExecManagerImpl Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1717
- **ZDI-CAN:** ZDI-CAN-24015
- **Date:** 2024-12-19
- **CVE:** CVE-2024-12829
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Arista
- **Affected Products:** NG Firewall
- **Credit:** Mehmet INCE (@mdisec) from PRODAFT
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1717/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Arista NG Firewall. Authentication is required to exploit this vulnerability. The specific flaw exists within the ExecManagerImpl class. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

07/03/24 – ZDI reported the vulnerability to the vendor 08/07/24 – the vendor’s security team asked ZDI to re-send the vulnerability 11/12/24 - ZDI re-submitted the report to the vendor 11/18/24 - ZDI asked for updates 11/21/24 - ZDI asked for updates 12/10/24 - ZDI notified the vendor of the intention to publish the case as a 0-day advisory Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application

## Disclosure Timeline

- 2024-07-03 - Vulnerability reported to vendor
- 2024-12-19 - Coordinated public release of advisory
- 2024-12-19 - Advisory Updated
