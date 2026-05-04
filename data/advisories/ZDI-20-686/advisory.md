# ZDI-20-686: (Pwn2Own) Inductive Automation Ignition getDiffs Deserialization Of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-686
- **ZDI-CAN:** ZDI-CAN-10276
- **Date:** 2020-06-01
- **CVE:** CVE-2020-10644
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Inductive Automation
- **Affected Products:** Ignition
- **Credit:** Team FLASHBACK: Pedro Ribeiro (pedrib@gmail.com|@pedrib1337) and Radek Domanski (@RabbitPro)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-686/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Inductive Automation Ignition. Authentication is not required to exploit this vulnerability. The specific flaw exists with the handling of project diffs. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this to execute code in the context of SYSTEM.

## Additional Details

Inductive Automation has issued an update to correct this vulnerability. More details can be found at: https://www.us-cert.gov/ics/advisories/icsa-20-147-01

## Disclosure Timeline

- 2020-01-30 - Vulnerability reported to vendor
- 2020-06-01 - Coordinated public release of advisory
- 2021-06-29 - Advisory Updated
