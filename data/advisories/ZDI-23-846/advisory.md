# ZDI-23-846: (Pwn2Own) Western Digital MyCloud PR4100 Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-846
- **ZDI-CAN:** ZDI-CAN-19860
- **Date:** 2023-06-08
- **CVE:** CVE-2022-36331
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Western Digital
- **Affected Products:** MyCloud PR4100
- **Credit:** Claroty Research - Vera Mens, Noam Moshe, Uri Katz, Sharon Brizinov
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-846/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Western Digital MyCloud PR4100 NAS devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the generation of TLS certificates. The issue results from the inclusion of sensitive information in publicly accessible channels. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of root.

## Additional Details

Western Digital has issued an update to correct this vulnerability. More details can be found at: https://www.westerndigital.com/support/product-security/wdc-22020-my-cloud-os-5-my-cloud-home-ibi-firmware-update

## Disclosure Timeline

- 2023-01-24 - Vulnerability reported to vendor
- 2023-06-08 - Coordinated public release of advisory
