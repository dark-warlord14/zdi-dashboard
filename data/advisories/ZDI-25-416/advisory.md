# ZDI-25-416: ServiceStack FindType Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-416
- **ZDI-CAN:** ZDI-CAN-25837
- **Date:** 2025-06-23
- **CVE:** CVE-2025-6445
- **CVSS:** 8.1
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** ServiceStack
- **Affected Products:** ServiceStack
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-416/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of ServiceStack. Interaction with this library is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the implementation of the FindType method. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

ServiceStack has issued an update to correct this vulnerability. More details can be found at: https://docs.servicestack.net/releases/v8_06#reported-vulnerabilities

## Disclosure Timeline

- 2024-11-19 - Vulnerability reported to vendor
- 2025-06-23 - Coordinated public release of advisory
- 2025-06-23 - Advisory Updated
