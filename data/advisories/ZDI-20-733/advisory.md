# ZDI-20-733: (Pwn2Own) Rockwell Automation FactoryTalk Linx CopyRenameProject Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-733
- **ZDI-CAN:** ZDI-CAN-10292
- **Date:** 2020-06-22
- **CVE:** CVE-2020-12001
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Rockwell Automation
- **Affected Products:** FactoryTalk Linx
- **Credit:** Chris Anastasio (muffin) and Steven Seeley (mr_me) of Incite Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-733/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Rockwell Automation Studio 5000. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of the CopyRenameProject parameter provided to hmi_isapi.dll. The issue results from the lack of proper validation of user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Rockwell Automation has issued an update to correct this vulnerability. More details can be found at: https://rockwellautomation.custhelp.com/app/answers/detail/a_id/1126945

## Disclosure Timeline

- 2020-01-30 - Vulnerability reported to vendor
- 2020-06-22 - Coordinated public release of advisory
- 2020-06-23 - Advisory Updated
