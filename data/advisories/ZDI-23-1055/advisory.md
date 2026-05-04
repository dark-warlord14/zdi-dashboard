# ZDI-23-1055: (Pwn2Own) Softing Secure Integration Server Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1055
- **ZDI-CAN:** ZDI-CAN-20550
- **Date:** 2023-08-09
- **CVE:** CVE-2023-29377
- **CVSS:** 6.6
- **CVSS Vector:** AV:N/AC:H/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Softing
- **Affected Products:** Secure Integration Server
- **Credit:** Claroty Research - Team82 - Uri Katz, Noam Moshe, Vera Mens, Sharon Brizinov
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1055/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Softing Secure Integration Server. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the handling of OPC UA FileDirectory FileType renames. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of root.

## Additional Details

Softing has issued an update to correct this vulnerability. More details can be found at: https://industrial.softing.com/fileadmin/psirt/downloads/syt-2023-2.html

## Disclosure Timeline

- 2023-02-22 - Vulnerability reported to vendor
- 2023-08-09 - Coordinated public release of advisory
