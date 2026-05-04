# ZDI-20-685: (Pwn2Own) Inductive Automation Ignition getDiffs Missing Authentication for Critical Function Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-685
- **ZDI-CAN:** ZDI-CAN-10275
- **Date:** 2020-06-01
- **CVE:** CVE-2020-12004
- **CVSS:** 5.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N
- **Affected Vendors:** Inductive Automation
- **Affected Products:** Ignition
- **Credit:** Pedro Ribeiro (pedrib@gmail.com) and Radek Domanski (radek.domanski@gmail.com)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-685/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Inductive Automation Ignition. Authentication is not required to exploit this vulnerability. The specific flaw exists within the getDiffs method of the com.inductiveautomation.ignition.gateway.servlets.gateway.functions.ProjectDownload class. The issue results from the lack of proper authentication required to query to server. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of SYSTEM.

## Additional Details

Inductive Automation has issued an update to correct this vulnerability. More details can be found at: https://www.us-cert.gov/ics/advisories/icsa-20-147-01

## Disclosure Timeline

- 2020-02-04 - Vulnerability reported to vendor
- 2020-06-01 - Coordinated public release of advisory
- 2021-06-29 - Advisory Updated
