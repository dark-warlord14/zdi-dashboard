# ZDI-23-1287: TP-Link Tapo C210 ActiveCells Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1287
- **ZDI-CAN:** ZDI-CAN-20589
- **Date:** 2023-08-31
- **CVE:** CVE-2023-41184
- **CVSS:** 6.8
- **CVSS Vector:** AV:A/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** TP-Link
- **Affected Products:** Tapo C210
- **Credit:** Cyrille Chatras
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1287/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of TP-Link Tapo C210 IP cameras. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the handling of the ActiveCells parameter of the CreateRules and ModifyRules APIs. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Fixed in firmware: 1.3.6 Build 230426 Rel.48373n https://www.tp-link.com/en/support/download/tapo-c210/#Firmware-Release-Notes

## Disclosure Timeline

- 2023-03-15 - Vulnerability reported to vendor
- 2023-08-31 - Coordinated public release of advisory
