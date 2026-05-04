# ZDI-20-1448: (Pwn2Own) Western Digital MyCloud PR4100 nasAdmin Incorrect Authorization Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1448
- **ZDI-CAN:** ZDI-CAN-12385
- **Date:** 2020-12-16
- **CVE:** CVE-2020-28970
- **CVSS:** 0.0
- **CVSS Vector:** AV:P/AC:H/PR:H/UI:R/S:U/C:N/I:N/A:N
- **Affected Vendors:** Western Digital
- **Affected Products:** MyCloud PR4100
- **Credit:** Sam Thomas (@_s_n_t) of Pentest Ltd (@pentestltd)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1448/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass authentication on affected installations of Western Digital MyCloud PR4100. Authentication is not required to exploit this vulnerability. The specific flaw exists within the nasAdmin service, which listens on TCP port 80 and 443 by default. The issue results from incorrect string matching logic when accessing protected pages. An attacker can leverage this vulnerability to execute arbitrary code in the context of root.

## Additional Details

Western Digital has issued an update to correct this vulnerability. More details can be found at: https://www.westerndigital.com/support/productsecurity/wdc-20009-os5-firmware-5-06-115

## Disclosure Timeline

- 2020-11-06 - Vulnerability reported to vendor
- 2020-12-16 - Coordinated public release of advisory
