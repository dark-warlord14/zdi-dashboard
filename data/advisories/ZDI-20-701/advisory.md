# ZDI-20-701: (0Day) (Pwn2Own) Apple macOS Quarantine Attribute Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-701
- **ZDI-CAN:** ZDI-CAN-10776
- **Date:** 2020-06-09
- **CVE:** N/A
- **CVSS:** 5.3
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** @SSLab_Gatech (@jinmo123, @setuid0x0_, and @insu_yun_en)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-701/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of downloaded files. The issue results from the improper validation of user authorization to perform operations on a quarantined file. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges and execute code in the context of root.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with ZDI policies. 03/19/20 – ZDI disclosed the report to the vendor live in the Pwn2Own virtual disclosure room 05/21/20 – The vendor advised ZDI that: “We are not treating ZDI-CAN-10776 as a security issue.” 05/29/20 – ZDI advised the vendor of the intent to publish the report as a 0-day advisory on 06/09/20 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the service. Only the clients and servers that have a legitimate procedural relationship with the service should be permitted to communicate with it.

## Disclosure Timeline

- 2020-06-09 - Vulnerability reported to vendor
- 2020-06-09 - Coordinated public release of advisory
- 2021-06-29 - Advisory Updated
