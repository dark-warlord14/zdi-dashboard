# ZDI-20-1216: Micro Focus Operations Bridge Reporter JMX Missing Authentication Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1216
- **ZDI-CAN:** ZDI-CAN-11071
- **Date:** 2020-09-23
- **CVE:** CVE-2020-11856
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Micro Focus
- **Affected Products:** Operations Bridge Reporter
- **Credit:** Pedro Ribeiro (pedrib@gmail.com|@pedrib1337) from Agile Information Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1216/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Micro Focus Operations Bridge Reporter. Authentication is not required to exploit this vulnerability. The specific flaw exists within the configuration of the JMX remote interface. This interface allows a remote attacker to register attacker-controlled MBeans. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Micro Focus has issued an update to correct this vulnerability. More details can be found at: https://softwaresupport.softwaregrp.com/doc/KM03710590

## Disclosure Timeline

- 2020-05-27 - Vulnerability reported to vendor
- 2020-09-23 - Coordinated public release of advisory
