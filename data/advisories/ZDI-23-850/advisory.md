# ZDI-23-850: (Pwn2Own) Western Digital MyCloud PR4100 RESTSDK Server-Side Request Forgery Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-850
- **ZDI-CAN:** ZDI-CAN-19767
- **Date:** 2023-06-08
- **CVE:** CVE-2022-29840
- **CVSS:** 7.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Western Digital
- **Affected Products:** MyCloud PR4100
- **Credit:** Sam Thomas (@_s_n_t) of Pentest Ltd (@pentestltd)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-850/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Western Digital MyCloud PR4100 NAS devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the RESTSDK server. The issue results from the lack of proper validation of a URI prior to accessing resources. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of root.

## Additional Details

Western Digital has issued an update to correct this vulnerability. More details can be found at: https://www.westerndigital.com/support/product-security/wdc-23006-my-cloud-firmware-version-5-26-202

## Disclosure Timeline

- 2022-12-29 - Vulnerability reported to vendor
- 2023-06-08 - Coordinated public release of advisory
