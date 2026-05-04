# ZDI-25-732: (Pwn2Own) Lorex 2K Indoor Wi-Fi Security Camera Improper Validation of Array Index Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-732
- **ZDI-CAN:** ZDI-CAN-25639
- **Date:** 2025-07-30
- **CVE:** CVE-2025-8389
- **CVSS:** 7.5
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Lorex
- **Affected Products:** 2K Indoor Wi-Fi Security Camera
- **Credit:** phudq and namnp from Viettel Cyber Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-732/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Lorex 2K Indoor Wi-Fi Security Cameras. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of requests sent to TCP port 9876. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an array. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of root.

## Additional Details

Fixed in Firmware Version V2.800.0000000.8.R.20241111

## Disclosure Timeline

- 2025-01-08 - Vulnerability reported to vendor
- 2025-07-30 - Coordinated public release of advisory
- 2025-07-30 - Advisory Updated
