# ZDI-23-1625: TP-Link Archer A54 libcmm.so dm_fillObjByStr Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1625
- **ZDI-CAN:** ZDI-CAN-22262
- **Date:** 2023-11-14
- **CVE:** CVE-2023-44448
- **CVSS:** 6.8
- **CVSS Vector:** AV:A/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** TP-Link
- **Affected Products:** Archer A54
- **Credit:** Nicholas Zubrisky and Peter Girnus of Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1625/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of TP-Link Archer A54 routers. Authentication is required to exploit this vulnerability. The specific flaw exists within the file libcmm.so. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Fixed in TL-WR902AC(EU)_V1_231027 and TL-WR902AC(US)_V1_231025 https://www.tp-link.com/en/support/download/tl-wr902ac/v1/#Firmware https://www.tp-link.com/us/support/download/tl-wr902ac/v1/#Firmware

## Disclosure Timeline

- 2023-10-03 - Vulnerability reported to vendor
- 2023-11-14 - Coordinated public release of advisory
