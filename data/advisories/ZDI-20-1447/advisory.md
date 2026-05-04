# ZDI-20-1447: (Pwn2Own) Western Digital MyCloud PR4100 nasAdmin Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1447
- **ZDI-CAN:** ZDI-CAN-12327
- **Date:** 2020-12-15
- **CVE:** CVE-2020-28971
- **CVSS:** 5.4
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:N
- **Affected Vendors:** Western Digital
- **Affected Products:** MyCloud PR4100
- **Credit:** Carlos Su from DEVCORE Security Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1447/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass authentication on affected installations of Western Digital MyCloud PR4100. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the nasAdmin service, which listens on TCP port 80 and 443 by default. The issue results from incorrect string matching logic when accessing protected pages. An attacker can leverage this vulnerability to execute arbitrary code in the context of root.

## Additional Details

Western Digital has issued an update to correct this vulnerability. More details can be found at: https://www.westerndigital.com/support/productsecurity/wdc-20009-os5-firmware-5-06-115

## Disclosure Timeline

- 2020-12-15 - Vulnerability reported to vendor
- 2020-12-15 - Coordinated public release of advisory
