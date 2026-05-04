# ZDI-20-731: (Pwn2Own) Rockwell Automation FactoryTalk View SE Project File Parsing Out-Of-Bounds Access Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-731
- **ZDI-CAN:** ZDI-CAN-10270
- **Date:** 2020-06-22
- **CVE:** CVE-2020-12031
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Rockwell Automation
- **Affected Products:** FactoryTalk View SE
- **Credit:** Tobias Scharnowski (@ScepticCtf), Niklas Breitfeld (@brymko), Ali Abbasi (@bl4ckic3), researchers at the Chair for Systems Security (SysSec) at Ruhr-University Bochum
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-731/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Rockwell Automation FactoryTalk View SE. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of project files. The issue results from the lack of proper validation of user-supplied data, which can result in a memory access past the end of an allocated object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Rockwell Automation has issued an update to correct this vulnerability. More details can be found at: https://rockwellautomation.custhelp.com/app/answers/detail/a_id/1126944

## Disclosure Timeline

- 2020-03-26 - Vulnerability reported to vendor
- 2020-06-22 - Coordinated public release of advisory
- 2021-06-29 - Advisory Updated
