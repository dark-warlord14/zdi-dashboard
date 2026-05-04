# ZDI-23-668: (Pwn2Own) Lexmark MC3224i fax_change_faxtrace_setting Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-668
- **ZDI-CAN:** ZDI-CAN-19470
- **Date:** 2023-05-17
- **CVE:** CVE-2023-26067
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Lexmark
- **Affected Products:** MC3224i
- **Credit:** James Horseman and Zach Hanley of Horizon3 A.I.
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-668/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Lexmark MC3224i printers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the fax_change_faxtrace_settings script. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of the httpd user.

## Additional Details

Lexmark has issued an update to correct this vulnerability. More details can be found at: https://publications.lexmark.com/publications/security-alerts/CVE-2023-26067.pdf

## Disclosure Timeline

- 2022-12-28 - Vulnerability reported to vendor
- 2023-05-17 - Coordinated public release of advisory
