# ZDI-25-415: ServiceStack GetErrorResponse Improper Input Validation NTLM Relay Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-415
- **ZDI-CAN:** ZDI-CAN-25834
- **Date:** 2025-06-23
- **CVE:** CVE-2025-6444
- **CVSS:** 5.9
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** ServiceStack
- **Affected Products:** ServiceStack
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-415/
## Vulnerability Details

This vulnerability allows remote attackers to relay NTLM credentials on affected installations of ServiceStack. Interaction with this library is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the implementation of the GetErrorResponse method. The issue results from the lack of proper validation of user-supplied data, which can result in a type confusion condition. An attacker can leverage this vulnerability to relay NTLM credentials in the context of the current user.

## Additional Details

ServiceStack has issued an update to correct this vulnerability. More details can be found at: https://docs.servicestack.net/releases/v8_06#reported-vulnerabilities

## Disclosure Timeline

- 2024-11-19 - Vulnerability reported to vendor
- 2025-06-23 - Coordinated public release of advisory
- 2025-06-23 - Advisory Updated
