# ZDI-26-041: (0Day) (Pwn2Own) Enel X JuiceBox 40 Telnet Service Missing Authentication Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-041
- **ZDI-CAN:** ZDI-CAN-23285
- **Date:** 2026-01-09
- **CVE:** CVE-2026-0778
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Enel X
- **Affected Products:** JuiceBox 40
- **Credit:** ZDI team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-041/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Enel X JuiceBox 40 charging stations. Authentication is not required to exploit this vulnerability. The specific flaw exists within the telnet service, which listens on TCP port 2000 by default. The issue results from the lack of authentication prior to allowing remote connections. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

02/22/24 - ZDI submitted the report to the vendor’s security contact in North America 06/03/24 - ZDI asked for updates 06/16/25 – ZDI reached out to the vendor's cert team 06/20/25 – the cert team requested an extension until 12/31/25 06/25/25 – ZDI approved on an extension until 10/25/25 11/07/25 – ZDI asked for the fix 11/12/25 – the vendor requested an extension until June 2026 12/18/25 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product

## Disclosure Timeline

- 2025-06-27 - Vulnerability reported to vendor
- 2026-01-09 - Coordinated public release of advisory
- 2026-01-09 - Advisory Updated
