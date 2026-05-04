# ZDI-20-290: Quest Foglight Evolve CommandLineService Use of Hard-coded Credentials Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-290
- **ZDI-CAN:** ZDI-CAN-9553
- **Date:** 2020-03-12
- **CVE:** CVE-2020-8868
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Quest
- **Affected Products:** Foglight Evolve
- **Credit:** rgod of 9sg
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-290/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Quest Foglight Evolve. Authentication is not required to exploit this vulnerability. The specific flaw exists within the __service__ user account. The product contains a hard-coded password for this account. An attacker can leverage this vulnerability to execute arbitrary code in the context of SYSTEM.

## Additional Details

Quest has issued an update to correct this vulnerability. More details can be found at: https://support.quest.com/foglight/kb/315091/fms-5-9-5-hotfix-hfix-314

## Disclosure Timeline

- 2019-12-13 - Vulnerability reported to vendor
- 2020-03-12 - Coordinated public release of advisory
