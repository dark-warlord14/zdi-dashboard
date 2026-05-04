# ZDI-25-809: (0Day) Microsoft Exchange PowerShell Exposed Dangerous Method NTLM Relay Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-809
- **ZDI-CAN:** ZDI-CAN-23450
- **Date:** 2025-08-06
- **CVE:** N/A
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Exchange
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-809/
## Vulnerability Details

This vulnerability allows remote attackers to relay NTLM credentials on affected installations of Microsoft Exchange. Authentication is required to exploit this vulnerability. The specific flaw exists within the PowerShell backend. The issue results from an exposed dangerous method. An attacker can leverage this vulnerability to relay NTLM credentials in the context of SYSTEM.

## Additional Details

02/21/24 – ZDI reported the vulnerability to the vendor. 03/19/24 – The vendor assessed the case as low severity. 07/30/25 – ZDI Informed the vendor that we plan to publish the case as a zero-day advisory on 08/06/25. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product.

## Disclosure Timeline

- 2024-02-21 - Vulnerability reported to vendor
- 2025-08-06 - Coordinated public release of advisory
- 2025-08-06 - Advisory Updated
