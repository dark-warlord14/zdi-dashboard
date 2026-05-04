# ZDI-20-1445: (Pwn2Own) Western Digital MyCloud PR4100 nasAdmin Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1445
- **ZDI-CAN:** ZDI-CAN-12214
- **Date:** 2020-12-15
- **CVE:** CVE-2020-28940
- **CVSS:** 5.4
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:N
- **Affected Vendors:** Western Digital
- **Affected Products:** MyCloud PR4100
- **Credit:** Lays (@_L4ys)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1445/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass authentication on affected installations of Western Digital MyCloud PR4100. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the nasAdmin service, which listens on TCP port 80 and 443 by default. The issue results from incorrect string matching logic when accessing protected pages. An attacker can leverage this vulnerability to execute arbitrary code in the context of root.

## Additional Details

Western Digital has issued an update to correct this vulnerability. More details can be found at: https://www.westerndigital.com/support/productsecurity/wdc-20009-os5-firmware-5-06-115

## Disclosure Timeline

- 2020-11-05 - Vulnerability reported to vendor
- 2020-12-15 - Coordinated public release of advisory
