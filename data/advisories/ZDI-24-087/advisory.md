# ZDI-24-087: (Pwn2Own) Western Digital MyCloud PR4100 RESTSDK Server-Side Request Forgery Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-087
- **ZDI-CAN:** ZDI-CAN-22456
- **Date:** 2024-02-06
- **CVE:** CVE-2023-22817
- **CVSS:** 6.3
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Western Digital
- **Affected Products:** MyCloud PR4100
- **Credit:** @_s_n_t of @pentestltd
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-087/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Western Digital MyCloud PR4100 NAS devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the RESTSDK server. The issue results from the lack of proper validation of a URI prior to accessing resources. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of root.

## Additional Details

Western Digital has issued an update to correct this vulnerability. More details can be found at: https://www.westerndigital.com/support/product-security/wdc-24001-western-digital-my-cloud-os-5-my-cloud-home-duo-and-sandisk-ibi-firmware-update

## Disclosure Timeline

- 2023-11-09 - Vulnerability reported to vendor
- 2024-02-06 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
