# ZDI-23-1809: TP-Link TL-WR902AC dm_fillObjByStr Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1809
- **ZDI-CAN:** ZDI-CAN-21819
- **Date:** 2023-12-19
- **CVE:** CVE-2023-50225
- **CVSS:** 6.8
- **CVSS Vector:** AV:A/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** TP-Link
- **Affected Products:** TL-WR902AC
- **Credit:** Nicholas Zubrisky and Peter Girnus of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1809/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of TP-Link TL-WR902AC routers. Authentication is required to exploit this vulnerability. The specific flaw exists within the libcmm.so module. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

TP-Link has issued an update to correct this vulnerability. More details can be found at: https://www.tp-link.com/ca/support/download/tl-wr902ac/v3/#Firmware

## Disclosure Timeline

- 2023-07-26 - Vulnerability reported to vendor
- 2023-12-19 - Coordinated public release of advisory
