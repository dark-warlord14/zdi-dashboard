# ZDI-23-003: Microsoft Exchange PowerShell Unsafe Reflection NTLM Relay Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-003
- **ZDI-CAN:** ZDI-CAN-19042
- **Date:** 2024-10-16
- **CVE:** CVE-2023-21745
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Exchange
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-003/
## Vulnerability Details

This vulnerability allows remote attackers to relay NTLM credentials on affected installations of Microsoft Exchange. Authentication is required to exploit this vulnerability. The specific flaw exists within the PowerShell endpoint. The process does not properly restrict a user-supplied argument before using it to create an instance of an object. An attacker can leverage this vulnerability to relay NTLM credentials in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-21745

## Disclosure Timeline

- 2022-09-29 - Vulnerability reported to vendor
- 2024-10-16 - Coordinated public release of advisory
- 2024-10-16 - Advisory Updated
