# ZDI-22-347: (Pwn2Own) Western Digital MyCloud PR4100 nasAdmin Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-347
- **ZDI-CAN:** ZDI-CAN-15888
- **Date:** 2022-02-15
- **CVE:** CVE-2022-22990
- **CVSS:** 6.3
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Western Digital
- **Affected Products:** MyCloud PR4100
- **Credit:** Sam Thomas (@_s_n_t) of Pentest Ltd (@pentestltd)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-347/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass authentication on affected installations of Western Digital MyCloud PR4100. Authentication is not required to exploit this vulnerability. The specific flaw exists within the nasAdmin service, which listens on TCP ports 80 and 443 by default. The issue results from incorrect string matching logic when accessing protected pages. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Western Digital has issued an update to correct this vulnerability. More details can be found at: https://www.westerndigital.com/support/product-security/wdc-22002-my-cloud-os5-firmware-5-19-117

## Disclosure Timeline

- 2021-12-01 - Vulnerability reported to vendor
- 2022-02-15 - Coordinated public release of advisory
