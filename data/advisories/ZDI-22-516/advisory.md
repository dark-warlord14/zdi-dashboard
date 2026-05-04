# ZDI-22-516: (Pwn2Own) Canon imageCLASS MF644Cdw privet Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-516
- **ZDI-CAN:** ZDI-CAN-15834
- **Date:** 2022-03-18
- **CVE:** CVE-2022-24674
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Canon
- **Affected Products:** imageCLASS MF644Cdw
- **Credit:** Nicolas Devillers ( @nikaiw ), Jean-Romain Garnier and Raphael Rigo ( @_trou_ )
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-516/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Canon imageCLASS MF644Cdw printers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the privet API. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Canon has issued an update to correct this vulnerability. More details can be found at: https://www.usa.canon.com/internet/portal/us/home/support/product-advisories/detail/canon-laser-printer-and-small-office-multifunctional-printer-measure-against-buffer-overflow/

## Disclosure Timeline

- 2022-01-21 - Vulnerability reported to vendor
- 2022-03-18 - Coordinated public release of advisory
- 2023-03-08 - Advisory Updated
