# ZDI-25-408: PEAK-System Driver PCANFD_ADD_FILTERS Time-Of-Check Time-Of-Use Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-408
- **ZDI-CAN:** ZDI-CAN-24161
- **Date:** 2025-06-18
- **CVE:** CVE-2025-6217
- **CVSS:** 3.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:L/I:N/A:N
- **Affected Vendors:** PEAK-System
- **Affected Products:** Driver
- **Credit:** Viacheslav Moskvin
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-408/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of PEAK-System Driver. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of the PCANFD_ADD_FILTERS IOCTL. The issue results from the lack of proper locking when performing operations on an object. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the kernel.

## Additional Details

Fixed in version 8.19.0 https://www.peak-system.com/Details.114+M5f4e1a41c28.0.html?&L=1

## Disclosure Timeline

- 2024-08-12 - Vulnerability reported to vendor
- 2025-06-18 - Coordinated public release of advisory
- 2025-06-18 - Advisory Updated
