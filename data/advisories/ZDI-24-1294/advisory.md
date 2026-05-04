# ZDI-24-1294: Western Digital MyCloud PR4100 ddns-start Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1294
- **ZDI-CAN:** ZDI-CAN-22537
- **Date:** 2024-09-26
- **CVE:** CVE-2024-22170
- **CVSS:** 7.5
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Western Digital
- **Affected Products:** MyCloud PR4100
- **Credit:** Claroty Research - Team82 - Noam Moshe
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1294/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Western Digital MyCloud PR4100. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of HTTP responses provided to the ddns-start program. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length, heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the device.

## Additional Details

Western Digital has issued an update to correct this vulnerability. More details can be found at: https://www.westerndigital.com/support/product-security/wdc-24005-western-digital-my-cloud-os-5-firmware-5-29-102

## Disclosure Timeline

- 2024-05-28 - Vulnerability reported to vendor
- 2024-09-26 - Coordinated public release of advisory
- 2024-09-26 - Advisory Updated
