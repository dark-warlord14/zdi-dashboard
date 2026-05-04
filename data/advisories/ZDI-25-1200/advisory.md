# ZDI-25-1200: (0Day) Anritsu ShockLine SCPI Race Condition Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1200
- **ZDI-CAN:** ZDI-CAN-27315
- **Date:** 2025-12-30
- **CVE:** CVE-2025-15349
- **CVSS:** 7.5
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Anritsu
- **Affected Products:** ShockLine
- **Credit:** kimiya
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1200/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Anritsu ShockLine. Authentication is not required to exploit this vulnerability. The specific flaw exists within the SCPI component. The issue results from the lack of proper locking when performing operations on an object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

07/15/25 – ZDI submitted the report to the vendor 09/11/25 – ZDI asked for updates 09/12/25 – the vendor acknowledged the receipt of the report 10/10/25 – ZDI asked for the fix 12/10/25 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory on 12/30/25 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product

## Disclosure Timeline

- 2025-07-15 - Vulnerability reported to vendor
- 2025-12-30 - Coordinated public release of advisory
- 2025-12-30 - Advisory Updated
