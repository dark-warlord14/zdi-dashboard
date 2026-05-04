# ZDI-20-729: (Pwn2Own) Rockwell Automation FactoryTalk View SE Backup Missing Authentication for Critical Function Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-729
- **ZDI-CAN:** ZDI-CAN-10283
- **Date:** 2020-06-22
- **CVE:** CVE-2020-12028
- **CVSS:** 7.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Rockwell Automation
- **Affected Products:** FactoryTalk View SE
- **Credit:** Team FLASHBACK: Pedro Ribeiro (pedrib@gmail.com|@pedrib1337) and Radek Domanski (@RabbitPro)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-729/
## Vulnerability Details

This vulnerability allows remote attackers to create arbitrary files on affected installations of Rockwell Automation FactoryTalk View SE. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of project backups. The issue results from lack of authorization prior to initiating a backup. An attacker can leverage this in conjunction with other vulnerability to execute code in the context of SYSTEM.

## Additional Details

Rockwell Automation has issued an update to correct this vulnerability. More details can be found at: https://rockwellautomation.custhelp.com/app/answers/detail/a_id/1126944

## Disclosure Timeline

- 2020-01-30 - Vulnerability reported to vendor
- 2020-06-22 - Coordinated public release of advisory
- 2021-06-29 - Advisory Updated
