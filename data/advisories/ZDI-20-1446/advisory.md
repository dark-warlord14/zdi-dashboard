# ZDI-20-1446: (Pwn2Own) Western Digital MyCloud PR4100 nasAdmin Incorrect Authorization Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1446
- **ZDI-CAN:** ZDI-CAN-12465
- **Date:** 2020-12-15
- **CVE:** CVE-2020-29563
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Western Digital
- **Affected Products:** MyCloud PR4100
- **Credit:** orangetw
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1446/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Western Digital MyCloud PR4100. Authentication is not required to exploit this vulnerability. The specific flaw exists within the mod_rewrite module. The issue results from the way the software parses URLs to make authorization decisions. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Western Digital has issued an update to correct this vulnerability. More details can be found at: https://www.westerndigital.com/support/productsecurity/wdc-20010-my-cloud-os5-firmware-5-07-118

## Disclosure Timeline

- 2020-12-15 - Vulnerability reported to vendor
- 2020-12-15 - Coordinated public release of advisory
