# ZDI-22-1601: Microsoft Exchange ApprovedApplication Exposed Dangerous Method NTLM Relay Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1601
- **ZDI-CAN:** ZDI-CAN-18881
- **Date:** 2024-10-16
- **CVE:** CVE-2022-41078
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Exchange
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1601/
## Vulnerability Details

This vulnerability allows remote attackers to relay NTLM credentials on affected installations of Microsoft Exchange. Authentication is required to exploit this vulnerability. The specific flaw exists within the ApprovedApplication class. The issue results from an exposed dangerous method. An attacker can leverage this vulnerability to relay NTLM credentials in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-41078

## Disclosure Timeline

- 2022-09-20 - Vulnerability reported to vendor
- 2024-10-16 - Coordinated public release of advisory
- 2024-10-16 - Advisory Updated
