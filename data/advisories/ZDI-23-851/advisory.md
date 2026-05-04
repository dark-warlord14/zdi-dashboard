# ZDI-23-851: (Pwn2Own) Western Digital MyCloud PR4100 RESTSDK Uncontrolled Resource Consumption Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-851
- **ZDI-CAN:** ZDI-CAN-19856
- **Date:** 2023-06-08
- **CVE:** CVE-2022-36326
- **CVSS:** 6.5
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** Western Digital
- **Affected Products:** MyCloud PR4100
- **Credit:** Sam Thomas (@_s_n_t) of Pentest Ltd (@pentestltd)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-851/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to create a denial-of-service condition on affected installations of Western Digital MyCloud PR4100 NAS devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the RESTSDK server. The issue results from uncontrolled resource consumption. An attacker can leverage this vulnerability to create a denial-of-service condition on the device.

## Additional Details

Western Digital has issued an update to correct this vulnerability. More details can be found at: https://www.westerndigital.com/support/product-security/wdc-23006-my-cloud-firmware-version-5-26-202

## Disclosure Timeline

- 2022-12-29 - Vulnerability reported to vendor
- 2023-06-08 - Coordinated public release of advisory
