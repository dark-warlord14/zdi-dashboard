# ZDI-25-369: Trend Micro Endpoint Encryption PolicyValueTableSerializationBinder Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-369
- **ZDI-CAN:** ZDI-CAN-25507
- **Date:** 2025-06-11
- **CVE:** CVE-2025-49212
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Endpoint Encryption
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-369/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Trend Micro Endpoint Encryption. Authentication is not required to exploit this vulnerability. The specific flaw exists within the PolicyValueTableSerializationBinder class. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/en-US/solution/KA-0019928

## Disclosure Timeline

- 2024-10-11 - Vulnerability reported to vendor
- 2025-06-11 - Coordinated public release of advisory
- 2025-06-11 - Advisory Updated
