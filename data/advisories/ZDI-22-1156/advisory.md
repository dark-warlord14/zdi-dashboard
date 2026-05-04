# ZDI-22-1156: (Pwn2Own) Softing Secure Integration Server UnZipFolder Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1156
- **ZDI-CAN:** ZDI-CAN-17255
- **Date:** 2022-08-23
- **CVE:** CVE-2022-1373
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Softing
- **Affected Products:** Secure Integration Server
- **Credit:** Chris Anastasio (muffin) and Steven Seeley (mr_me) of Incite Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1156/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Softing Secure Integration Server. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the Zip::UnZipFolder method. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Softing has issued an update to correct this vulnerability. More details can be found at: https://industrial.softing.com/fileadmin/psirt/downloads/syt-2022-5.html

## Disclosure Timeline

- 2022-05-09 - Vulnerability reported to vendor
- 2022-08-23 - Coordinated public release of advisory
