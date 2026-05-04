# ZDI-25-589: Trend Micro Worry-Free Business Security Missing Authentication Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-589
- **ZDI-CAN:** ZDI-CAN-25342
- **Date:** 2025-07-11
- **CVE:** CVE-2025-53378
- **CVSS:** 7.6
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Worry-Free Business Security
- **Credit:** Nicolas Caluori
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-589/
## Vulnerability Details

This vulnerability allows remote attackers to hijack security agents on affected installations of Trend Micro Worry-Free Business Security. In most cases, user interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the agent activation API. The issue results from the lack of authentication prior to allowing access to functionality. An attacker can leverage this vulnerability to remove protections or create a denial-of-service condition on the system.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/en-US/solution/KA-0019936

## Disclosure Timeline

- 2025-02-21 - Vulnerability reported to vendor
- 2025-07-11 - Coordinated public release of advisory
- 2025-07-11 - Advisory Updated
