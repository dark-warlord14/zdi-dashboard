# ZDI-25-731: (Pwn2Own) Lorex 2K Indoor Wi-Fi Security Camera Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-731
- **ZDI-CAN:** ZDI-CAN-25537
- **Date:** 2025-07-30
- **CVE:** CVE-2024-52544
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Lorex
- **Affected Products:** 2K Indoor Wi-Fi Security Camera
- **Credit:** phudq and namnp from Viettel Cyber Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-731/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Lorex 2K Indoor Wi-Fi Security Cameras. Authentication is not required to exploit this vulnerability. The specific flaw exists within the sonia module. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Fixed in Firmware Version V2.800.0000000.8.R.20241111

## Disclosure Timeline

- 2024-11-20 - Vulnerability reported to vendor
- 2025-07-30 - Coordinated public release of advisory
- 2025-07-30 - Advisory Updated
