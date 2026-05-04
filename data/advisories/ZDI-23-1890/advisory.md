# ZDI-23-1890: (0Day) Voltronic Power ViewPower USBCommEx shutdown Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1890
- **ZDI-CAN:** ZDI-CAN-22071
- **Date:** 2023-12-20
- **CVE:** CVE-2023-51585
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Voltronic Power
- **Affected Products:** ViewPower
- **Credit:** 06fe5fd2bc53027c4a3b7e395af0b850e7b8a044
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1890/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Voltronic Power ViewPower Pro. User interaction is required to exploit this vulnerability in that an administrator must trigger a shutdown operation. The specific flaw exists within the shutdown method. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

08/03/23 – ZDI made multiple attempts to contact the vendor across sales, support, and professional networking channels, which yielded no response from the vendor. We also contacted CISA, who was unsuccessful in receiving a response from the vendor. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2023-11-17 - Vulnerability reported to vendor
- 2023-12-20 - Coordinated public release of advisory
