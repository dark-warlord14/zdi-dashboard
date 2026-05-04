# ZDI-23-847: (Pwn2Own) Western Digital MyCloud PR4100 Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-847
- **ZDI-CAN:** ZDI-CAN-19861
- **Date:** 2023-06-08
- **CVE:** CVE-2022-36331
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Western Digital
- **Affected Products:** MyCloud PR4100
- **Credit:** Claroty Research - Vera Mens, Noam Moshe, Uri Katz, Sharon Brizinov
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-847/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Western Digital MyCloud PR4100 NAS devices. Some user interaction is required to exploit this vulnerability. The specific flaw exists within the way the device connects with cloud services. The issue results from the lack of authentication prior to allowing access to functionality. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of root.

## Additional Details

Western Digital has issued an update to correct this vulnerability. More details can be found at: https://www.westerndigital.com/support/product-security/wdc-22020-my-cloud-os-5-my-cloud-home-ibi-firmware-update

## Disclosure Timeline

- 2023-01-25 - Vulnerability reported to vendor
- 2023-06-08 - Coordinated public release of advisory
