# ZDI-25-1056: (0Day) Microsoft ASP.NET SOAP Execution Restriction Bypass Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1056
- **ZDI-CAN:** ZDI-CAN-27220
- **Date:** 2025-12-10
- **CVE:** N/A
- **CVSS:** 5.0
- **CVSS Vector:** AV:N/AC:H/PR:L/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Microsoft
- **Affected Products:** .NET
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1056/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft ASP.NET. Authentication may be required to exploit this vulnerability depending upon configuration. Additionally, specific configuration is required. The specific flaw exists within the handling of SOAP web service definitions. A crafted uploaded file can bypass restrictions on code execution. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

06/25/25 - ZDI reported the vulnerability to the vendor 06/25/25 – the vendor acknowledged the receipt of the report 07/01/25 – the vendor communicated that the reported behavior was not a vulnerability 11/26/25 – ZDI notified the vendor of the intention to publish the cases as a 0-day advisory on 12/11/25 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product.

## Disclosure Timeline

- 2025-06-25 - Vulnerability reported to vendor
- 2025-12-10 - Coordinated public release of advisory
- 2025-12-10 - Advisory Updated
