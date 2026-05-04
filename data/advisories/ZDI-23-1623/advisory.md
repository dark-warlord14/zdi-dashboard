# ZDI-23-1623: TP-Link TL-WR902AC loginFs Improper Authentication Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1623
- **ZDI-CAN:** ZDI-CAN-21529
- **Date:** 2023-11-14
- **CVE:** CVE-2023-44447
- **CVSS:** 6.5
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** TP-Link
- **Affected Products:** TL-WR902AC
- **Credit:** Aleksandar Djurdjevic 'revengsmK'
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1623/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to disclose sensitive information on affected installations of TP-Link TL-WR902AC routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the httpd service, which listens on TCP port 80 by default. The issue results from improper authentication. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

Fixed in TL-WR902AC(EU)_V1_231027 and TL-WR902AC(US)_V1_231025 https://www.tp-link.com/en/support/download/tl-wr902ac/v1/#Firmware https://www.tp-link.com/us/support/download/tl-wr902ac/v1/#Firmware

## Disclosure Timeline

- 2023-08-03 - Vulnerability reported to vendor
- 2023-11-14 - Coordinated public release of advisory
