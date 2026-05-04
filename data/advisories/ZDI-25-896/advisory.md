# ZDI-25-896: (0Day) Wondershare Repairit SAS Token Incorrect Permission Assignment Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-896
- **ZDI-CAN:** ZDI-CAN-26892
- **Date:** 2025-10-08
- **CVE:** CVE-2025-10644
- **CVSS:** 9.4
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:L
- **Affected Vendors:** Wondershare
- **Affected Products:** Repairit
- **Credit:** Alfredo Oliveira and David Fiser of Trend Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-896/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on Wondershare Repairit. Authentication is not required to exploit this vulnerability. The specific flaw exists within the permissions granted to an SAS token. An attacker can leverage this vulnerability to launch a supply-chain attack and execute arbitrary code on customers' endpoints.

## Additional Details

04/14/25 – ZDI reported the vulnerability to the vendor’s security team 07/30/25 – ZDI asked for updates 08/12/25 - ZDI asked for updates 08/26/25 - ZDI notified the vendor of the intention to publish the case as a 0-day advisory -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product.

## Disclosure Timeline

- 2025-04-14 - Vulnerability reported to vendor
- 2025-10-08 - Coordinated public release of advisory
- 2025-10-08 - Advisory Updated
