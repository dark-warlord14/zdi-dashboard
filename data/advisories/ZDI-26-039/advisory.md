# ZDI-26-039: (0Day) WatchYourLAN Configuration Page Argument Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-039
- **ZDI-CAN:** ZDI-CAN-26708
- **Date:** 2026-01-09
- **CVE:** CVE-2026-0774
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** WatchYourLAN
- **Affected Products:** WatchYourLAN
- **Credit:** x.com/xnand_
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-039/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of WatchYourLAN. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of the arpstrs parameter. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

06/19/25– ZDI submitted the report to the vendor 07/04/25 – ZDI asked to confirm the receipt of the report 11/06/25 – ZDI asked for updates 12/10/25 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product

## Disclosure Timeline

- 2025-06-19 - Vulnerability reported to vendor
- 2026-01-09 - Coordinated public release of advisory
- 2026-01-09 - Advisory Updated
