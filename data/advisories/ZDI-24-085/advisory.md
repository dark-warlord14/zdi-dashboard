# ZDI-24-085: (Pwn2Own) TP-Link Omada ER605 DHCPv6 Client Options Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-085
- **ZDI-CAN:** ZDI-CAN-22420
- **Date:** 2024-02-05
- **CVE:** CVE-2024-1179
- **CVSS:** 7.5
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** TP-Link
- **Affected Products:** Omada ER605
- **Credit:** LJP (@ljp_tw) and YingMuo (@YingMuo), working with DEVCORE Internship Program
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-085/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of TP-Link Omada ER605 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of DHCP options. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Fixed in firmware: ER605(UN)_V2_2.2.4 Build 20240119

## Disclosure Timeline

- 2023-11-09 - Vulnerability reported to vendor
- 2024-02-05 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
