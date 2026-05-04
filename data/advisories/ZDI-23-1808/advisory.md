# ZDI-23-1808: TP-Link TL-WR841N dropbearpwd Improper Authentication Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1808
- **ZDI-CAN:** ZDI-CAN-19899
- **Date:** 2023-12-19
- **CVE:** CVE-2023-50224
- **CVSS:** 6.5
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** TP-Link
- **Affected Products:** TL-WR841N
- **Credit:** Aleksandar Djurdjevic 'revengsmK'
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1808/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to disclose sensitive information on affected installations of TP-Link TL-WR841N routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the httpd service, which listens on TCP port 80 by default. The issue results from improper authentication. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

TP-Link has issued an update to correct this vulnerability. More details can be found at: https://www.tp-link.com/en/support/download/tl-wr841n/v12/#Firmware

## Disclosure Timeline

- 2023-02-24 - Vulnerability reported to vendor
- 2023-12-19 - Coordinated public release of advisory
