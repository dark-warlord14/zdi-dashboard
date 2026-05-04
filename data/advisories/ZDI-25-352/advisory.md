# ZDI-25-352: Pioneer DMH-WT7600NEX Software Update Signing Insufficient Verification of Data Authenticity Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-352
- **ZDI-CAN:** ZDI-CAN-26079
- **Date:** 2025-06-11
- **CVE:** CVE-2025-5832
- **CVSS:** 6.8
- **CVSS Vector:** AV:P/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Pioneer
- **Affected Products:** DMH-WT7600NEX
- **Credit:** Dmitry "InfoSecDJ" Janushkevich of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-352/
## Vulnerability Details

This vulnerability allows physically present attackers to execute arbitrary code on affected installations of Pioneer DMH-WT7600NEX devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the software update verification process. The issue results from the lack of validating all the data in the software update. An attacker can leverage this vulnerability to execute code in the context of the device.

## Additional Details

Fixed in Version 3.07 https://www.pioneerelectronics.com/PUSA/Support/Downloads

## Disclosure Timeline

- 2025-01-14 - Vulnerability reported to vendor
- 2025-06-11 - Coordinated public release of advisory
- 2025-08-28 - Advisory Updated
