# ZDI-25-350: Pioneer DMH-WT7600NEX Root Filesystem Insufficient Verification of Data Authenticity Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-350
- **ZDI-CAN:** ZDI-CAN-26077
- **Date:** 2025-06-11
- **CVE:** CVE-2025-5833
- **CVSS:** 4.6
- **CVSS Vector:** AV:P/AC:L/PR:N/UI:N/S:U/C:N/I:H/A:N
- **Affected Vendors:** Pioneer
- **Affected Products:** DMH-WT7600NEX
- **Credit:** Dmitry "InfoSecDJ" Janushkevich of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-350/
## Vulnerability Details

This vulnerability allows physically present attackers to bypass authentication on affected installations of Pioneer DMH-WT7600NEX devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the configuration of the operating system. The issue results from the lack of properly configured protection for the root file system. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Fixed in Version 3.07 https://www.pioneerelectronics.com/PUSA/Support/Downloads

## Disclosure Timeline

- 2025-01-14 - Vulnerability reported to vendor
- 2025-06-11 - Coordinated public release of advisory
- 2025-08-28 - Advisory Updated
