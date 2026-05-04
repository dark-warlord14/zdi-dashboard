# ZDI-20-714: (0Day) (Pwn2Own) Inductive Automation Ignition ServerMessageHeader Deserialization of Untrusted Data Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-714
- **ZDI-CAN:** ZDI-CAN-10277
- **Date:** 2020-06-15
- **CVE:** N/A
- **CVSS:** 5.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N
- **Affected Vendors:** Inductive Automation
- **Affected Products:** Ignition
- **Credit:** Chris Anastasio (muffin) and Steven Seeley (mr_me) of Incite Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-714/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Inductive Automation Ignition. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of serialized data. The issue results in the lack of proper authentication required to query to server. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of SYSTEM.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 01/22/20 – ZDI disclosed the vulnerability report to the vendor onsite at Pwn2Own 04/22/20 – ZDI requested an update 04/23/20 – The vendor provided an update that the report was still in work 05/05/20 – ICS-CERT requested an update and the vendor replied no ETA was available 05/06/20 – ZDI agreed to wait until further notice 05/20/20 – ZDI requested an update and the vendor replied that there was no ETA 06/03/20 - ICS-CERT requested an update and the vendor replied no ETA was available 06/04/20 – ZDI notified the vendor and ICS-CERT that the report would be published as a 0-day advisory on 06/15/20 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the service to trusted machines. Only the clients and servers that have a legitimate procedural relationship with the service should be permitted to communicate with it. This could be accomplished in a number of ways, most notably with firewall rules/whitelisting.

## Disclosure Timeline

- 2020-01-30 - Vulnerability reported to vendor
- 2020-06-15 - Coordinated public release of advisory
