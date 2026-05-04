# ZDI-24-088: (Pwn2Own) Western Digital MyCloud PR4100 RESTSDK Uncontrolled Resource Consumption Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-088
- **ZDI-CAN:** ZDI-CAN-22440
- **Date:** 2024-02-06
- **CVE:** CVE-2023-22819
- **CVSS:** 5.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L
- **Affected Vendors:** Western Digital
- **Affected Products:** MyCloud PR4100
- **Credit:** @_s_n_t of @pentestltd
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-088/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Western Digital MyCloud PR4100 NAS devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the RESTSDK server. The issue results from uncontrolled resource consumption. An attacker can leverage this vulnerability to create a denial-of-service condition on the device.

## Additional Details

Western Digital has issued an update to correct this vulnerability. More details can be found at: https://www.westerndigital.com/support/product-security/wdc-24001-western-digital-my-cloud-os-5-my-cloud-home-duo-and-sandisk-ibi-firmware-update

## Disclosure Timeline

- 2023-11-09 - Vulnerability reported to vendor
- 2024-02-06 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
