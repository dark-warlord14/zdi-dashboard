# ZDI-25-360: Trend Micro Worry-Free Business Security Uncontrolled Search Path Element Arbitrary Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-360
- **ZDI-CAN:** ZDI-CAN-23056
- **Date:** 2025-06-11
- **CVE:** CVE-2025-49487
- **CVSS:** 6.8
- **CVSS Vector:** AV:P/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Worry-Free Business Security
- **Credit:** Will Dormann
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-360/
## Vulnerability Details

This vulnerability allows physically present attackers to execute arbitrary code on affected installations of Trend Micro Worry-Free Business Security. Authentication is not required to exploit this vulnerability. The specific flaw exists within the configuration of OpenSSL. The process loads an OpenSSL configuration file from an unsecured location. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/en-US/solution/KA-0019936

## Disclosure Timeline

- 2024-03-12 - Vulnerability reported to vendor
- 2025-06-11 - Coordinated public release of advisory
- 2025-06-11 - Advisory Updated
