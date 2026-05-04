# ZDI-23-1813: Inductive Automation Ignition ModuleInvoke Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1813
- **ZDI-CAN:** ZDI-CAN-21624
- **Date:** 2023-12-20
- **CVE:** CVE-2023-50218
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Inductive Automation
- **Affected Products:** Ignition
- **Credit:** Nguyen Quoc Viet (Petrus Viet) of VNG Security Researcher
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1813/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Inductive Automation Ignition. Authentication is required to exploit this vulnerability. The specific flaw exists within the ModuleInvoke class. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Inductive Automation has issued an update to correct this vulnerability. More details can be found at: https://security.inductiveautomation.com/?tcuUid=fc4c4515-046d-4365-b688-693337449c5b

## Disclosure Timeline

- 2023-08-09 - Vulnerability reported to vendor
- 2023-12-20 - Coordinated public release of advisory
- 2024-01-05 - Advisory Updated
