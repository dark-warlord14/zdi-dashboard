# ZDI-25-947: (0Day) Ivanti Endpoint Manager AgentPortal Deserialization of Untrusted Data Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-947
- **ZDI-CAN:** ZDI-CAN-25369
- **Date:** 2025-10-16
- **CVE:** CVE-2025-11622
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Ivanti
- **Affected Products:** Endpoint Manager
- **Credit:** 06fe5fd2bc53027c4a3b7e395af0b850e7b8a044
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-947/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Ivanti Endpoint Manager. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the AgentPortal service. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

11/05/24 – ZDI reported the vulnerability to the vendor 11/08/24 – the vendor acknowledged the receipt of the report 01/24/25 – the vendor confirmed the issue and requested an extension until the second half of 2025 05/06/25 – ZDI asked for updates 07/29/25 - the vendor communicated that the issue will be patched in November 2025 09/30/25 - ZDI notified the vendor of the intention to publish the case as a 0-day advisory 10/13/2025 - the vendor published a security advisory -- Mitigation: On 11/12/2025 the vendor published a fix for the vulnerability: https://forums.ivanti.com/s/article/Security-Advisory-EPM-November-2025-for-EPM-2024?language=en_US

## Disclosure Timeline

- 2024-11-05 - Vulnerability reported to vendor
- 2025-10-16 - Coordinated public release of advisory
- 2025-11-17 - Advisory Updated
