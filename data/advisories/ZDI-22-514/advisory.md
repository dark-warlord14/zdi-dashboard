# ZDI-22-514: (Pwn2Own) Canon imageCLASS MF644Cdw CADM Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-514
- **ZDI-CAN:** ZDI-CAN-15802
- **Date:** 2023-03-01
- **CVE:** CVE-2022-24672
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Canon
- **Affected Products:** imageCLASS MF644Cdw
- **Credit:** Mehdi Talbi (@abu_y0ussef), Remi Jullian (@netsecurity1), Thomas Jeunet (@cleptho), from @Synacktiv
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-514/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Canon imageCLASS MF644Cdw printers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the CADM service. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

Canon has issued an update to correct this vulnerability. More details can be found at: https://www.usa.canon.com/support/canon-product-advisories/canon-laser-printer-inkjet-printer-and-small-office-multifunctio

## Disclosure Timeline

- 2022-01-21 - Vulnerability reported to vendor
- 2023-03-01 - Coordinated public release of advisory
- 2023-03-01 - Advisory Updated
