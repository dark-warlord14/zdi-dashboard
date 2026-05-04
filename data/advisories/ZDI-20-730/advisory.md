# ZDI-20-730: (Pwn2Own) Rockwell Automation FactoryTalk View SE Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-730
- **ZDI-CAN:** ZDI-CAN-10284
- **Date:** 2020-06-22
- **CVE:** CVE-2020-12029
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Rockwell Automation
- **Affected Products:** FactoryTalk View SE
- **Credit:** Team FLASHBACK: Pedro Ribeiro (pedrib@gmail.com|@pedrib1337) and Radek Domanski (@RabbitPro)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-730/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Rockwell Automation FactoryTalk View SE. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of project files. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Rockwell Automation has issued an update to correct this vulnerability. More details can be found at: https://rockwellautomation.custhelp.com/app/answers/detail/a_id/1126944

## Disclosure Timeline

- 2020-01-30 - Vulnerability reported to vendor
- 2020-06-22 - Coordinated public release of advisory
