# ZDI-24-092: (Pwn2Own) Canon imageCLASS MF753Cdw rls-login Authorization Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-092
- **ZDI-CAN:** ZDI-CAN-22386
- **Date:** 2024-02-06
- **CVE:** CVE-2023-6232
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Canon
- **Affected Products:** imageCLASS MF753Cdw
- **Credit:** @quangnh89
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-092/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Canon imageCLASS MF753Cdw printers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the parsing of the Authorization header provided to the /mls/rls-login/basic endpoint. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the device.

## Additional Details

Canon has issued an update to correct this vulnerability. More details can be found at: https://www.canon-europe.com/support/product-security-latest-news/

## Disclosure Timeline

- 2023-11-09 - Vulnerability reported to vendor
- 2024-02-06 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
