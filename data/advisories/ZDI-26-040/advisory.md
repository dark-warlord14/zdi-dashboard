# ZDI-26-040: (0Day) Discord Client Uncontrolled Search Path Element Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-040
- **ZDI-CAN:** ZDI-CAN-27057
- **Date:** 2026-01-09
- **CVE:** CVE-2026-0776
- **CVSS:** 7.3
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Discord
- **Affected Products:** Client
- **Credit:** T. Doğa Gelişli
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-040/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Discord Client. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the discord_rpc module. The product loads a file from an unsecured location. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of a target user.

## Additional Details

07/08/25- ZDI submitted the report to the vendor 09/11/25 – ZDI asked to confirm the receipt of the report 09/15/25 – the vendor communicated that the reported behavior was not a vulnerability 12/01/25 – ZDI provided more information about the impact of the security issue 12/10/25 - ZDI asked for updates 12/11/25 - The vendor indicated that reported issue was out of scope for their bug bounty program 12/11/25 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product

## Disclosure Timeline

- 2025-07-08 - Vulnerability reported to vendor
- 2026-01-09 - Coordinated public release of advisory
- 2026-01-09 - Advisory Updated
